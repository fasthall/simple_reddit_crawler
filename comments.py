import praw
import csv
import time
import sys

reddit = praw.Reddit(client_id='', client_secret='', user_agent='simple_reddit_crawler', username='', password='')

input_file = open('posts_'+sys.argv[1]+'.csv', 'r')
input_file.readline()
reader = csv.reader(input_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

output_file = open('comments_'+sys.argv[1]+'.csv', 'w')
writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
keys = ['id', 'submission', 'score', 'body', 'created', 'author', 'author_flair_text']
writer.writerow(keys)

cnt_post = 0
cnt_comment = 0

for row in reader:
    print(cnt_post, cnt_comment)
    sys.stdout.flush()
    done = False
    while not done:
        try:
            buf = []
            submission = reddit.submission(id=row[1])
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                s = []
                for k in keys:
                    s.append(getattr(comment, k))
                buf.append(s)
                cnt_comment += 1
            writer.writerows(buf)
            cnt_post += 1
            done = True
        except:
            time.sleep(5)


input_file.close()
output_file.close()

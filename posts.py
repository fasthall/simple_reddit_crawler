import praw
import csv
import time
import sys

reddit = praw.Reddit(client_id='', client_secret='', user_agent='simple_reddit_crawler', username='', password='')

subreddit = reddit.subreddit(sys.argv[1])
print(subreddit.display_name)

output_file = open(sys.argv[1] + '.csv', 'w')
keys = ['title', 'id', 'score', 'upvote_ratio', 'created', 'author', 'author_flair_text',\
'num_comments', 'likes', 'is_self', 'selftext', 'url', 'quarantine', 'num_reports',\
'locked', 'link_flair_text', 'user_reports', 'permalink']
writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(keys)

cnt_total = 0
end = 1483228799 # 2016-12-31
togo = 365
while end - 86400 >= 1451606400: # 2016-01-01
    cnt_day = 0
    posts = []
    try:
        for submission in subreddit.submissions(end - 86400, end):
        # for submission in subreddit.new(limit = 10):
            s = []
            for key in keys:
                s.append(getattr(submission, key))
            posts.append(s)
            cnt_day += 1
        print(togo, end - 86400, '~', end, ':', cnt_day)
        sys.stdout.flush()
        writer.writerows(posts)
        cnt_total += cnt_day
        end -= 86400
        togo -= 1
    except:
        time.sleep(60)

print(cnt_total)
output_file.close()

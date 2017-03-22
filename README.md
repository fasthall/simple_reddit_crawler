# Simple Reddit Crawler
Simple crawler for reddit

## Setup
0. Have [Python](https://www.python.org/) and [PRAW](https://praw.readthedocs.io/en/latest/) installed.
1. Go to [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/) and crate an app. Remember the client ID and client secret.
2. Edit [posts.py](posts.py) and [comments.py](comments.py). Paste the ID and secret. Also enter the username and password.

## Run
    $ python posts.py subreddit
    (It generates a output file in csv format)
    $ python comments.py subreddit
    (It based on the generated posts file generate a comments list in another csv file)
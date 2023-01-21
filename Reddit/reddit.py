# import reddit dependencies
import praw
from praw.reddit import Reddit
from praw.models import MoreComments
# manage database
from tinydb import Query

import time
import config
import database

submission = Query()


def login():
    try:
        my_config = config.load_config()
        reddit = praw.Reddit(client_id=my_config['RedditCredential']['client_id'],
                             client_secret=my_config['RedditCredential']['client_secret'],
                             user_agent=my_config['RedditCredential']['user_agent'])

        print(f"Logged in to Reddit successfully!")
        return reddit
    except Exception as e:
        return e


def get_thread(reddit:Reddit, subreddit:str):

    subreddit_ = reddit.subreddit(subreddit)


    threads = subreddit_.top('week')

    # sort threads based on number of up-votes
    sorted_threads = sorted(threads, key=lambda x: int(x.score), reverse=True)

    chosen_thread = None

    # get the top most up-voted thread that is not in the database
    db = database.load_databse()
    for thread in sorted_threads:
        if not db.search(submission.id == str(thread.id)):
            db.insert({'id': thread.id, 'time': time.time()})
            db.close()
            print(f"Chosen thread: {thread.title} -- Score: {thread.score}")
            chosen_thread = thread
            db.close()
            break
    db.close()
    return chosen_thread


def get_comments(thread):
    my_config = config.load_config()
    topn = my_config['Reddit']['topn_comments']
    chosen_comments = None
    comments = []
    for top_level_comment in thread.comments:
        if len(comments) == topn:
            break
        if isinstance(top_level_comment, MoreComments):
            continue
        comments.append(top_level_comment)

    chosen_comments = comments
    print(f"{len(chosen_comments)} comments are chosen")
    return chosen_comments

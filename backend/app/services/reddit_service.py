import praw
from ..core.config import settings

def get_reddit_client():
    return praw.Reddit(
        client_id=settings.REDDIT_CLIENT_ID,
        client_secret=settings.REDDIT_CLIENT_SECRET,
        user_agent=settings.REDDIT_USER_AGENT
    )
def fetch_subreddit_posts(subreddit_name: str, limit: int = 100):
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    
    for post in subreddit.hot(limit=limit):
        # Get the top answer if it exists
        top_answer = ""
        post.comments.replace_more(limit=0)  # Load all comments
        if len(post.comments) > 0:
            # Get highest voted comment
            top_comment = max(post.comments, key=lambda x: x.score, default=None)
            if top_comment:
                top_answer = top_comment.body

        if '?' in post.title and top_answer:  # Only include posts with questions and answers
            posts.append({
                'title': post.title,
                'body': post.selftext,
                'answer': top_answer,  # This is the highest-voted comment
                'score': post.score
            })
    return posts

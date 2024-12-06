from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database
from .services import reddit_service
from .services.faq_generator import FAQGenerator
from .core.config import settings
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler = BackgroundScheduler()

def scheduled_faq_update():
    with database.SessionLocal() as db:
        subreddit = "osdev"
        posts = reddit_service.fetch_subreddit_posts(subreddit)
        print(f"Fetching posts from r/{subreddit}")
        faq_generator = FAQGenerator()
        print(f"Posts: {len(posts)}")
        faqs = faq_generator.generate_faq(posts)
        
        db.query(models.FAQ).delete()
        for faq in faqs:
            db_faq = models.FAQ(**faq)
            db.add(db_faq)
        db.commit()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup_event():
    print(f"fetching posts")
    database.init_db()
    scheduler.add_job(scheduled_faq_update, 'interval', hours=24)
    # scheduler.add_job(scheduled_faq_update, 'interval', minutes=5)
    scheduler.add_job(scheduled_faq_update, 'interval', seconds=10)
    scheduler.start()

@app.get("/api/faq")
def get_faqs(db: Session = Depends(get_db)):
    return db.query(models.FAQ).all()

@app.post("/api/update-faq")
def update_faq(subreddit: str, db: Session = Depends(get_db)):
    posts = reddit_service.fetch_subreddit_posts(subreddit)
    faq_generator = FAQGenerator()
    faqs = faq_generator.generate_faq(posts)
    
    db.query(models.FAQ).delete()
    for faq in faqs:
        db_faq = models.FAQ(**faq)
        db.add(db_faq)
    db.commit()
    
    return {"message": "FAQs updated successfully"}
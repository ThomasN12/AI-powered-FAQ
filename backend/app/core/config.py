# app/core/config.py
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
   PROJECT_NAME: str = "Reddit FAQ Generator"
   POSTGRES_USER: str
   POSTGRES_PASSWORD: str 
   POSTGRES_SERVER: str
   POSTGRES_PORT: str
   POSTGRES_DB: str
   REDDIT_CLIENT_ID: str
   REDDIT_CLIENT_SECRET: str
   REDDIT_USER_AGENT: str
   # OPENAI_API_KEY: str
   
   @property
   def DATABASE_URL(self):
       return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings(
   POSTGRES_USER=os.getenv("POSTGRES_USER"),
   POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD", ""),
   POSTGRES_SERVER=os.getenv("POSTGRES_SERVER", "localhost"),
   POSTGRES_PORT=os.getenv("POSTGRES_PORT", "5432"),
   POSTGRES_DB=os.getenv("POSTGRES_DB"),
   REDDIT_CLIENT_ID=os.getenv("REDDIT_CLIENT_ID"),
   REDDIT_CLIENT_SECRET=os.getenv("REDDIT_CLIENT_SECRET"), 
   REDDIT_USER_AGENT=os.getenv("REDDIT_USER_AGENT"),
   # OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
)
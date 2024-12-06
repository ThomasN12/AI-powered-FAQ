# backend/README.md

# FAQ Generator Backend

Backend service for the AI-powered FAQ generator system.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure environment variables (.env):

```
POSTGRES_USER=your_user
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=faqdb
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT="FAQ Generator 1.0"
```

3. Initialize database:

```sql
psql postgresql://user@localhost:5432
CREATE DATABASE faqdb;
```

4. Run the server:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

- GET /api/faq: Get all FAQs
- POST /api/update-faq: Trigger FAQ update

## Components

- reddit_service.py: Reddit data collection
- faq_generator.py: Question clustering and answer selection
- models.py: Database schema
- main.py: FastAPI application and endpoints

## Scheduled Updates

FAQs are automatically updated every 24 hours using APScheduler.

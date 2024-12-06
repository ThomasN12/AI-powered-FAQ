# Main README.md
# AI-Powered FAQ Generator

An automated system that generates and maintains a Frequently Asked Questions (FAQ) page by analyzing Reddit discussions. The system uses AI/ML techniques to cluster similar questions and identify the most relevant answers.

## Overview
This project implements an AI-powered FAQ system that:
- Collects questions and answers from Reddit
- Uses ML clustering to group similar questions
- Identifies best answers based on relevance and votes
- Updates automatically every 24 hours
- Presents organized Q&A through a clean web interface

## Technologies Used
### Backend
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- PRAW (Reddit API)
- scikit-learn (ML clustering)
- APScheduler (Automated updates)

### Frontend
- React with TypeScript
- Material-UI components
- Tailwind CSS

## AI/ML Components
1. **Text Vectorization (TF-IDF)**
   - Converts text questions into numerical vectors
   - Measures word importance across questions
   - Enables similarity comparisons

2. **K-means Clustering**
   - Groups similar questions automatically
   - Creates organized FAQ categories
   - Improves content accessibility

## Project Structure
```
reddit-faq-generator/
├── backend/         # FastAPI application
├── frontend/        # React application
└── docs/           # Documentation
```

## Getting Started
1. Clone the repository
2. Follow setup instructions in backend/README.md
3. Follow setup instructions in frontend/README.md

---

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

---

# frontend/README.md
# FAQ Generator Frontend

React-based frontend for displaying organized FAQs.

## Setup
1. Install dependencies:
```bash
npm install
```

2. Run development server:
```bash
npm start
```

## Features
- Accordion-style FAQ display
- Clear separation of questions and answers
- Related questions grouping
- Responsive design

## Components
- FAQList: Main component for displaying FAQs
- Accordion: Material-UI based expandable panels
- Custom styling with Tailwind CSS

## Styling
- Question content: Gray background
- Answers: Left border with blue accent
- Related questions: Separated section
- Responsive layout for all screen sizes

## Build
```bash
npm run build
```

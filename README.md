# AI-Powered FAQ Generator

An automated system that generates and maintains a Frequently Asked Questions (FAQ) page by analyzing Reddit discussions. The system uses AI/ML techniques to cluster similar questions and identify the most relevant answers.

## Overview

This project implements an AI-powered FAQ system that:

- Collects questions and answers from Reddit
- Uses ML clustering to group similar questions
- Identifies best answers based on relevance and votes
- Updates automatically every 24 hours
- Presents organized Q&A through a web interface

<!-- ## Technologies Used

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
- Tailwind CSS -->

## AI/ML Components

1. **Text Vectorization (TF-IDF)**

   - Converts text questions into numerical vectors
   - Measures word importance across questions
   - Enables similarity comparisons

2. **K-means Clustering**
   - Groups similar questions automatically
   - Creates organized FAQ categories
   <!-- - Improves content accessibility -->

## Project Structure

```
reddit-faq-generator/
├── backend/         # FastAPI application
├── frontend/        # React application
```

## Getting Started

1. Clone the repository
2. Follow setup instructions in backend/README.md
3. Follow setup instructions in frontend/README.md

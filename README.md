# AI Backend Internship Project

I built this project to demonstrate three practical backend skills often tested in internships:

1. Building a recommendation endpoint using machine learning basics
2. Exposing webhook-friendly APIs for workflow tools such as n8n
3. Creating domain-specific text embeddings for LLM and SLM workflows

## What This Project Does

- Accepts a user query and returns relevant catalog items using TF-IDF + cosine similarity
- Accepts text and returns a vector representation suitable for downstream retrieval experiments
- Accepts webhook event payloads for event-driven integration patterns

## Tech Stack

- Python
- FastAPI
- Pandas, NumPy
- Scikit-learn
- n8n compatible webhook flow

## Structure

- app/main.py: FastAPI routes and app setup
- app/services.py: recommendation and embedding logic
- app/schemas.py: request models
- data/products.csv: sample domain dataset
- workflows/n8n_webhook_recommendation.json: example n8n flow

## Run Locally

1. Create and activate a virtual environment
2. Install dependencies from requirements.txt
3. Start the API with uvicorn

Commands:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

Docs URL after startup:
http://127.0.0.1:8000/docs

## Endpoints

- POST /recommend
- POST /embed
- POST /webhooks/events

## Sample Payloads

POST /recommend
{
  "query": "python api backend",
  "top_k": 3
}

POST /embed
{
  "text": "agentic workflow with embeddings"
}

## Future Improvements

- Add authentication and rate limiting
- Add persistent query analytics
- Add automated tests and CI checks

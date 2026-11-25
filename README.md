# AI Backend Internship Project

I built this project to practise a few backend patterns that are useful in AI application work: a catalogue recommendation endpoint, text-vector generation, and a webhook-style API route.

The API is built with FastAPI. The current recommendation and vector logic uses scikit-learn's TF-IDF vectorizer and cosine similarity; it does not use a transformer embedding model.

## What is implemented

- `POST /recommend` — ranks catalogue items against a text query.
- `POST /embed` — returns the TF-IDF vector dimensions and the first 10 values.
- `POST /webhooks/events` — accepts an event payload and returns its source, event type, and payload keys.
- `GET /ui` — serves the browser interface.
- `GET /` — returns basic API information.

The recommendation data is loaded from `data/products.csv`. The service combines each product's title, category, and tags before fitting the TF-IDF vectorizer.

## Technology

- Python
- FastAPI and Pydantic
- pandas and NumPy
- scikit-learn
- TF-IDF and cosine similarity

## Project structure

```text
AI-Backened-Internship-Project/
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── services.py
├── data/
│   └── products.csv
├── ui/
│   └── index.html
├── requirements.txt
└── README.md
```

## Run locally

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Then open:

- API documentation: http://127.0.0.1:8000/docs
- Browser interface: http://127.0.0.1:8000/ui

These addresses are local to the machine running the API.

## Example requests

`POST /recommend`

```json
{
  "query": "python api backend",
  "top_k": 3
}
```

`POST /embed`

```json
{
  "text": "agentic workflow with text retrieval"
}
```

`POST /webhooks/events`

```json
{
  "source": "n8n",
  "event_type": "order.created",
  "payload": {
    "order_id": 123
  }
}
```

## Current limitations

- Recommendation is based on TF-IDF lexical features, not contextual transformer embeddings.
- The webhook route acknowledges the received event; it does not currently trigger an external workflow.
- The API uses the sample CSV catalogue.
- I have not recorded automated test results or a live deployment for this repository.

## Possible next steps

- Add tests for the API routes and recommendation logic.
- Add persistent event handling if the webhook flow needs to trigger downstream work.
- Evaluate retrieval quality against a small set of labelled queries.
- Consider a transformer-based embedding model as a separate retrieval experiment.

## Author

**Afzal Hussain** · [@Afzu01](https://github.com/Afzu01)

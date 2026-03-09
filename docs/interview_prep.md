# Interview Prep

## 60-Second Intro

I built a backend project that combines recommendation, webhook integration, and embedding extraction. The API is implemented with FastAPI and structured into route, schema, and service layers. For recommendations, I used TF-IDF with cosine similarity as a fast and interpretable baseline. I also added endpoints for webhook event handling and text embedding extraction to demonstrate LLM/SLM integration readiness.

## 3-Minute Project Walkthrough

1. Problem:
I wanted to demonstrate practical backend skills that map to real internship responsibilities: recommendation logic, REST APIs, and event-driven integration.

2. Architecture:
- app/main.py contains API routes
- app/schemas.py validates requests
- app/services.py contains recommendation and embedding logic
- data/products.csv provides a sample domain corpus

3. Recommendation logic:
- Build TF-IDF vectors on product title, category, and tags
- Transform user query into vector
- Compute cosine similarity
- Return top-k ranked results

4. Embedding logic:
- Reuse fitted TF-IDF vectorizer
- Convert text into vector output
- Return dimensions and vector preview

5. Webhook logic:
- Receive source, event_type, and payload
- Validate and return structured acknowledgement

6. Improvements planned:
- Add persistent storage
- Add hybrid recommendation with collaborative signal
- Add auth, logging, and tests

## Technical Deep-Dive Questions You May Get

1. Why TF-IDF first, not deep learning embeddings?
Because it is fast to build, interpretable, and effective as a baseline for smaller datasets.

2. How does cosine similarity help?
It compares vector direction, so relevance is based on term composition, not just raw frequency.

3. How would you scale this?
Pre-compute vectors, cache query results, move storage to a DB/vector store, add async workers.

4. How do webhooks fit into backend systems?
They allow external systems to trigger your backend on events, enabling event-driven automation.

5. What backend fundamentals did you apply?
Request validation, modular design, endpoint contracts, and reproducible environment setup.

## Behavioral Answers (Short)

1. Founder's mindset:
I take ownership end to end: define scope, ship a working baseline, and iterate with measurable improvements.

2. Fast-paced environment:
I break work into deliverables, prioritize critical path tasks, and communicate blockers early.

3. Autonomy:
I can independently implement API features and debug integration issues while keeping documentation clear.

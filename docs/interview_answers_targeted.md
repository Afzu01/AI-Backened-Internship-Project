# Targeted Interview Answers (expLocal + NEAILabs)

## 1. Tell me about yourself (45 seconds)

I am a backend-focused student developer who enjoys building practical API systems and taking ownership from design to implementation. Recently, I built a project that combines recommendation logic, webhook-ready integration, and embedding extraction for LLM/SLM style workflows. I like fast execution, clear documentation, and measurable iteration.

## 2. Why this internship?

I want a role where I can contribute to real backend systems instead of only academic coding. Your internship focuses on ownership, API quality, and integration depth, which matches how I like to work.

## 3. Explain your recommendation system design

I created a content-based recommendation baseline using TF-IDF vectorization and cosine similarity. Product title, category, and tags are transformed into vectors. User query is vectorized and compared against catalog vectors, then top-k ranked results are returned.

## 4. How did you implement agentic workflow compatibility?

I exposed webhook-friendly endpoints with structured payload contracts and prepared an n8n flow file that receives external events, calls the recommendation API, and returns the response in an event-driven sequence.

## 5. How did you approach embeddings?

I added a domain-text embedding endpoint that converts input text into vector output using a fitted vectorizer. This acts as a practical baseline for retrieval and semantic matching pipelines.

## 6. What did you own end to end?

I handled project setup, API design, request schema validation, service logic, data file preparation, workflow integration artifact, docs, and submission packaging.

## 7. How do you handle fast-paced ambiguity?

I break tasks into deliverables, ship a stable baseline first, and improve iteratively. I keep communication clear through concise checkpoints and documentation.

## 8. expLocal-specific Go question: You are stronger in Python, how will you adapt?

I am currently backend-strong in Python and I am actively upskilling Go syntax, HTTP handlers, and concurrency concepts. I can contribute immediately on API architecture and integration while ramping quickly into Go implementation standards.

## 9. What would you improve next in your project?

- Add auth and API rate limiting
- Add persistent storage and query logging
- Add test coverage and CI checks
- Improve ranking with hybrid recommendation signals

## 10. Any question for interviewer?

What would be the first production problem you would want this intern to solve in the first two weeks?

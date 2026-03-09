from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CatalogService:
    def __init__(self) -> None:
        data_path = Path(__file__).resolve().parent.parent / "data" / "products.csv"
        self.df = pd.read_csv(data_path)
        self.df["text"] = (
            self.df["title"].fillna("")
            + " "
            + self.df["category"].fillna("")
            + " "
            + self.df["tags"].fillna("")
        )
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.df["text"])

    def recommend(self, query: str, top_k: int = 3) -> list[dict]:
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix).flatten()
        ranked_idx = scores.argsort()[::-1][:top_k]

        recommendations = []
        for idx in ranked_idx:
            row = self.df.iloc[idx]
            recommendations.append(
                {
                    "product_id": int(row["product_id"]),
                    "title": row["title"],
                    "category": row["category"],
                    "score": round(float(scores[idx]), 4),
                }
            )
        return recommendations

    def embed(self, text: str) -> list[float]:
        vec = self.vectorizer.transform([text]).toarray()[0]
        return vec.tolist()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
class PaperSearchEngine:
    def __init__(self,papers_df):
        self.papers_df = papers_df
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.document_vectors = self.vectorizer.fit_transform(papers_df["content"])
    def search(self, query, top_k=5):
        query_vector = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_vector, self.document_vectors).flatten()
        top_indices = similarity_scores.argsort()[::-1][:top_k]
        results = self.papers_df.iloc[top_indices][["title", "abstract"]]
        return results
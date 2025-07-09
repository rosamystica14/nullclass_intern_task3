from data_loader import load_cs_data
from search_engine import PaperSearchEngine

papers = load_cs_data()
engine = PaperSearchEngine(papers)

query = "neural networks for image recognition"
results = engine.search(query)

for i, row in results.iterrows():
    print(f"Title:{row['title']}")
    print(f"Abstract:{row['abstract'][:300]}...\n")
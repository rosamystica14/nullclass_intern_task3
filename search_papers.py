import pandas as pd

def load_filtered_data():
    return pd.read_csv("filtered_cs_papers.csv")  # or your filtered file

def search_papers(query):
    df = load_filtered_data()
    query = query.lower()
    results = df[df['title'].str.lower().str.contains(query) | df['abstract'].str.lower().str.contains(query)]
    return results[['title', 'abstract']].head(3).to_dict(orient='records')

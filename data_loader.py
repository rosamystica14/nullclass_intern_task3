import pandas as pd
def load_cs_data(file_path='filtered_cs_papers.csv',limit=1000):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['title','abstract'])
    df = df.head(limit)
    df["content"]=df["title"]+". "+df["abstract"]
    return df
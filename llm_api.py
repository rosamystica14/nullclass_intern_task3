import requests
from dotenv import load_dotenv 
import os

load_dotenv() 



API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"


headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print ("Status code:",response.status_code)
    print ("Raw response:",response.text)
    try:
        return response.json()
    except Exception as e:
        print("⚠️ API returned invalid response:", response.text)
        return {"error": "Invalid JSON"}

def get_llm_response(prompt):
    data = query({"inputs": prompt})
    if "error" in data:
        return "Error from model"
    return data[0].get("summary_text","No output")

# 🤖 ResearchBot – AI Scientific Assistant

This is a Streamlit-based chatbot that:
- Searches **Computer Science research papers** from arXiv
- Uses LLM to generate simplified explanations
- Allows users to **rate responses**
- Stores interactions in a CSV log

---

---

## 🔁 Similarity Notice: Task 1 & Task 2

This Task 3 project builds on concepts from **Task 1 (searching arXiv papers)** and **Task 2 (LLM-based explanation)** as part of the internship series. Certain modules and logic—such as:

- `search_papers.py` → Adapted from Task 1
- `llm_api.py`, `llm_explainer.py` → Inspired by Task 2
- Reused utility functions and data handling techniques

were **reused or improved** for better modularity and integration in this combined app.

This reuse is intentional as the tasks are designed to **build progressively**. All reused code is either authored by me during prior tasks or openly permitted for internal reuse.

---
⚠️ Note: This project uses Hugging Face (or OpenAI) APIs. Please set your API key inside llm_api.py or through environment variables (HF_API_TOKEN or OPENAI_API_KEY) before running the app.
LLM summaries are generated using Hugging Face's `facebook/bart-large-cnn` model securely via API. The token is managed using `.env` file to avoid exposure.



### 1. Clone or Download the Repo

```bash
git clone <your-repo-url>
cd nullclass_intern_task3

### Launch the App

streamlit run main_app.py

### Testing
Run test files individually using:

python test_loader.py
python test_search.py


# 📊 Features

🔍 Search CS papers by keyword

🧠 LLM response for abstracts

❤️ User feedback stored (timestamped)

📊 Analytics tab shows charts

# arxiv dataset google drive link
https://drive.google.com/file/d/1j10c_b_hyGvLnMfJKX5pPZThxhVTh3FG/view?usp=drive_link

# log csv drive link
https://drive.google.com/file/d/1y8pgljJEYN7XFgevPJjV_t4iKneQ0Rbg/view?usp=drive_link

# notebook link (jupyter)
https://drive.google.com/file/d/1bpuU1qx34JbWIghGDe-yKLGAL289PMZm/view?usp=drive_link

#filtered_cs_paper

https://drive.google.com/file/d/14jD4T1EU2dPFb7Oisjli9Nk6rXsAdvVD/view?usp=drive_link
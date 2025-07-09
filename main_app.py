# main_app.py
# author : ROSA MYSTICA.M
import streamlit as st
import pandas as pd
import os
from llm_api import get_llm_response
from analytics import store_user_data 
from search_papers import search_papers 

st.set_page_config(page_title="📚 ResearchBot", page_icon="🤖")
st.title("🤖 ResearchBot - Your AI Scientific Assistant")
st.subheader("🔬 Ask about any computer science concept or research topic!")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712107.png", width=100)
    st.header("🧭 Navigation")
    menu = st.selectbox("💡 Choose:", ["💬 Chatbot", "📊 Analytics"])

# Initialize session state
for key in ["last_rating", "submitted"]:
    if key not in st.session_state:
        st.session_state[key] = False if key == "submitted" else 0

if menu == "💬 Chatbot":
    st.markdown("### 🔍 What concept or topic are you exploring?")
    user_question = st.text_input("💬 Enter a CS research-related question:")

    if "last_rating" not in st.session_state:
        st.session_state.last_rating = 0
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if st.button("Search"):
        if user_question:
            with st.spinner("🔎 Searching arXiv papers..."):
                st.session_state.results = search_papers(user_question)
                if not st.session_state.results:
                    st.warning("❌ Sorry, no relevant papers found.")
                    st.session_state.user_question = user_question
                    st.session_state.response = "No relevant paper found."
                    st.session_state.topic = "Unknown"
                    st.session_state.submitted = True
                    st.session_state.rating_logged = False
                    
                else:
                    titles = [paper["title"] for paper in st.session_state.results]
                    st.session_state.submitted = True
                    st.session_state.selected_title = titles[0]

    if st.session_state.submitted:
        titles = [paper["title"] for paper in st.session_state.results]
        selected_title = st.selectbox("📄 Select a paper title:", titles, key="title_dropdown")

        selected_paper = next((p for p in st.session_state.results if p["title"] == selected_title), None)
        if selected_paper:
            st.success(f"📄 Title: {selected_paper['title']}")
            st.info(f"📝 Abstract: {selected_paper['abstract']}")

            # ✅ Only generate LLM explanation once
            if "response" not in st.session_state or st.session_state.user_question != user_question:
                with st.spinner("🧠 Generating explanation using LLM..."):
                    explanation = get_llm_response(selected_paper["abstract"])
                    st.session_state.response = explanation
                    st.session_state.user_question = user_question
                    st.session_state.topic = "Computer Science"
                    st.session_state.rating_logged = False

            st.markdown("### 🧠 Explanation:")
            st.write(st.session_state.response)

        # Rating slider
        rating = st.slider("🧡 How helpful was the explanation?", 1, 5, key="rating_slider")

        # ✅ Only store once and only if not logged before
        if not st.session_state.get("rating_logged", False) and rating != st.session_state.last_rating:
            st.session_state.last_rating = rating
            store_user_data(
                st.session_state.user_question,
                st.session_state.response,
                st.session_state.topic,
                rating
            )
            st.session_state.rating_logged = True



elif menu == "📊 Analytics":
    st.subheader("📊 User Interaction Summary:")
    try:
        df = pd.read_csv("data/log.csv")
        if not df.empty:
            allowed_topics = ["Computer Science", "Unknown"]
            filtered_df = df[df["topic"].isin(allowed_topics)]

            st.metric("📌 Total Questions", len(filtered_df))
            st.bar_chart(filtered_df["topic"].value_counts())
            st.metric("⭐ Avg. Satisfaction", round(filtered_df["rating"].mean(), 2))
        else:
            st.info("📂 No data available yet.")
    except FileNotFoundError:
        st.warning("🚫 No log file found.")
import streamlit as st
from recommendation import (
    content_based_recommend,
    hybrid_recommendation
)

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

mode = st.selectbox(
    "Choose Recommendation Type:",
    ["Content-Based", "Hybrid"]
)

if mode == "Content-Based":
    movie = st.text_input("Enter movie title:")
    
    if st.button("Recommend"):
        if movie.strip() == "":
            st.warning("Please enter a movie title.")
        else:
            results = content_based_recommend(movie)
            st.subheader("Recommended Movies:")
            for r in results:
                st.write("• " + r)

elif mode == "Hybrid":
    user_id = st.number_input("Enter User ID:", min_value=1, step=1)
    movie = st.text_input("Enter movie title:")

    if st.button("Recommend"):
        if movie.strip() == "":
            st.warning("Please enter a movie title.")
        else:
            results = hybrid_recommendation(user_id, movie)
            st.subheader("Hybrid Recommendations:")
            for r in results:
                st.write("• " + r)

# Movie Recommendation System (Hybrid)

An AI-powered movie recommendation system built using Content-Based Filtering, Collaborative Filtering, and a Hybrid Model, with a simple Streamlit web app for user interaction.

## Project Overview

This project processes and analyzes the TMDb 5000 Movies Dataset to build a recommendation engine capable of:

✔ Content-Based Filtering
Recommends movies similar to a chosen movie based on:
* Genres
* Keywords
* Cast
* Crew
* Overview
* Custom generated tags using TF-IDF & cosine similarity

✔ Collaborative Filtering (Simplified)
* Uses sample user ratings to approximate user preference patterns.

✔ Hybrid Recommendation
* Combines both similarity scores and predicted user ratings to generate more personalized results.

## Streamlit
The final interactive web interface is built with Streamlit.

## Features
* Content-Based Recommendations (based on movie metadata such as genres, description, cast)
* Collaborative Filtering (based on user ratings)
* Hybrid Recommendation Model
* Search movies by title
* Simple and interactive Streamlit UI
* Modular code structure (app.py + recommendation.py)
* Clean and scalable architecture for real projects

## Technologies Used
* Python
* Pandas, NumPy
* Scikit-learn (TF-IDF, cosine similarity)
* NLTK (Stemming)
* Streamlit
 Pickle

## Datasets
Initial
* 
* 
Processeed
processed_movies.csv

## Streamlit Usage
Run the app
- streamlit run app.py

## Future Improvements
* Deep Learning–based Collaborative Filtering (NCF)
* Mood-based recommendations
* Voice-enabled movie search
* Integration with a conversational AI chatbot

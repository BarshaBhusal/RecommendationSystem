import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load processed dataset
movies_df = pd.read_csv("processed_movies.csv")

# Load similarity matrix
similarity = pickle.load(open("similarity.pkl", "rb"))

# Load TF-IDF vectorizer 
tfidf = pickle.load(open("tfidf.pkl", "rb"))


def content_based_recommend(movie_title, top_n=10):
    movie_title = movie_title.lower()

    # Check movie exists
    if movie_title not in movies_df['title'].str.lower().values:
        return [f"Movie '{movie_title}' not found."]

    # Get index of movie
    idx = movies_df[movies_df['title'].str.lower() == movie_title].index[0]

    # Get similarity scores
    distances = similarity[idx]

    # Sort and get top N
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:top_n+1]

    recommendations = [movies_df.iloc[i[0]].title for i in movie_list]
    return recommendations

def predict_rating(user_id, movie_id):
    # Demo random score (since no real model is trained)
    import random
    return random.uniform(3.0, 5.0)


def hybrid_recommendation(user_id, movie_title, top_n=10):
    movie_title_lower = movie_title.lower()

    if movie_title_lower not in movies_df['title'].str.lower().values:
        return [f"Movie '{movie_title}' not found."]

    # Content-based part
    idx = movies_df[movies_df['title'].str.lower() == movie_title_lower].index[0]
    distances = similarity[idx]

    sim_scores = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:50]

    # Hybrid scoring = 50% content + 50% collaborative
    hybrid_scores = []
    for i, sim_score in sim_scores:
        movie_id = movies_df.iloc[i]['movie_id']
        cf_score = predict_rating(user_id, movie_id) / 5
        hybrid_score = 0.5 * sim_score + 0.5 * cf_score
        hybrid_scores.append((i, hybrid_score))

    hybrid_scores = sorted(hybrid_scores, key=lambda x: x[1], reverse=True)
    recommended = [movies_df.iloc[i[0]].title for i in hybrid_scores[:top_n]]
    return recommended

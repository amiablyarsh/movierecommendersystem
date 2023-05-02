import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import requests



def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=1775573aeee4de11befcfbdf9ecef273&language=en-US'.format(str(movie_id))
    response = requests.get(url)
    data = response.json()
    path = 'https://image.tmdb.org/t/p/w500'+data['poster_path']
    return path

cv = CountVectorizer(max_features=5000, stop_words='english')

new_df = pickle.load(open('movies.pkl', 'rb'))

vectors = cv.fit_transform(new_df['tags']).toarray()
vectors.shape

similarity = cosine_similarity(vectors)
similarity.shape
def recommend(movie):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, 
                        key = lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = new_df.iloc[i[0]].id
        recommended_movies.append(new_df.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movies_posters.append(poster)
    return recommended_movies, recommended_movies_posters
import streamlit as st
import pickle
import pandas as pd
import recommender

st.title('Movie Recommender System')

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

selected_movie_name = st.selectbox('Select a Movie',
                      movies_list)

if st.button('Recommend'):
    names, posters = recommender.recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
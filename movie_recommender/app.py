import streamlit as st
import pickle
import pandas as pd
import requests

def fp(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a18c4e288f9cb1f4a701e343ed46cb92&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(movie_id)

    return recommended_movies,recommended_movies_posters

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Please enter the name of movie', movies['title'].values)

if st.button('Recommend'):
   names,movie_ids=recommend(selected_movie_name)

   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(fp(movie_ids[0]))
   with col2:
       st.text(names[1])
       st.image(fp(movie_ids[1]))
   with col3:
       st.text(names[2])
       st.image(fp(movie_ids[2]))
   with col4:
       st.text(names[3])
       st.image(fp(movie_ids[3]))
   with col5:
       st.text(names[4])
       st.image(fp(movie_ids[4]))



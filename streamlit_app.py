import streamlit as st
import pickle
import pandas as pd
import requests
# from streamlit_lottie import st_lottie




movies_dict = pickle.load(open('movie_hindi.pkl','rb'))
movies = pd.DataFrame(movies_dict)
# lottie_image = "https://lottie.host/26e5a54a-bd7d-4df9-a1f1-e7c7f895eb48/h2WDQmr1CZ.json"
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# animation = load_lottieurl(lottie_image)

similarity = pickle.load(open('similarity_hindi.pkl','rb'))

# Set page configuration
st.set_page_config(page_title="Movie Recommender System", layout="wide",page_icon=":popcorn:")

left_column , right_column = st.columns([3, 1])
# st.title("Movie Recommender System")
# st.markdown('Discover your next favorite movie based on your preferences!')


# with right_column:
#     if animation:
#         st_lottie(animation, height=200, key="lottie")
def get_movie_poster(imdb_id): 
    # line 34 to 45 mera galat hai yeh wala 
    api_key = '6cf0b049'
    
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and data['Response'] == 'True':
        return data.get('Poster')
    else:
        return 'Movie not found or an error occurred'

# Example usage
# imdb_id = 'tt1630029'  # The IMDb ID for "The Shawshank Redemption"
  

# poster_url = get_movie_poster(imdb_id)
# print(poster_url)

def recommend(movie):
    movie_index = movies[movies['movie_name'] == movie].index[0]

    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    recommended_movie_name = []
    recommended_movie_posters = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_name.append(movies.iloc[i[0]].movie_name)
        # fetchposters
        recommended_movie_posters.append(get_movie_poster(movie_id))
    return recommended_movie_name,recommended_movie_posters
with left_column:
    st.title("Movie Recommender System")
    st.markdown('Discover your next favorite movie based on your preferences!')
    selected_movie = st.selectbox(
        "Please Select a Movie",movies['movie_name'].values
    )
if st.button("Recommend"):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



import streamlit as st
import pandas as pd
import pickle
movie_dict=pickle.load(open("movie_dict.pkl", "rb"))
distance=pickle.load(open("distance.pkl", "rb"))
movies=pd.DataFrame(movie_dict)
def recommend(movie):
    index=movies[movies["title"]==movie].index[0]
    recommended_movie=sorted(enumerate(distance[index]), reverse=True, key= lambda x: x[1])[1:6]
    recommended_list = []
    for item in recommended_movie:
        recommended_list.append(movies.iloc[item[0]]["title"])
    return recommended_list
st.title("Movie Recommendation")
option = st.selectbox(
    "Search your Movie",
    movies["title"].values
)
if st.button("Recommend"):
    for values in recommend(option):
        st.write(values)
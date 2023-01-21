import streamlit as st
import pandas as pd
st.set_page_config(page title="Song Recommendation", layout="wide")

from sklearn.neighbors import NearestNeighborsimport plotly.express as px
import streamlit.components.v1 as components

# Caching the function for loading the preprocessed data for faster loading time
@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv("data/filtered_track_df.csv")
    df['genres'] = df.genres.apply(lambda x: [i[1:-1] for i in str(x)[1:-1].split(", ")])
    exploded_track_df = df.explode("genres")
    return exploded_track_df
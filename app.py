import streamlit as st
import pandas as pd
import os
form io import BytesIO



#set up our App
st.set_page_config(page_title="Data sweeper", page_icon=":smiley:", layout="wide")
st.title("Data sweeper")
st.write("Transform your files between Csv and Excel formats. Upload your file and download the transformed file.")

uploaded_files = st.file_uploader("Choose a file", type=["csv", "xlsx"],
accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:                       )
        file_ext = os.path.splitext(file.name)[-1].lower()
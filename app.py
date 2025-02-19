import streamlit as st
import pandas as pd
import os
from io import BytesIO



#set up our App
st.set_page_config(page_title="Data sweeper", page_icon=":smiley:", layout="wide")
st.title("Data sweeper")
st.write("Transform your files between Csv and Excel formats. Upload your file and download the transformed file.")

uploaded_files = st.file_uploader("Choose a file", type=["csv", "xlsx"],
accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:                       )
    file_ext = os.path.splitext(file.name)[-1].lower()


    if file_ext == ".csv":
        df = pd.read_csv(file)
    elif file_ext == ".xlsx":
        df = pd.read_excel(file)
    else:
        st.error("Unsupported file type: {file_ext}")
        continue

    #Display infor about the life
    st.write(f"**File name:** {file.name}")
    st.write(f"**File size:** {file.size/1024}")

    #show 5 rows our df
    st.write("Preview the Head of the Dataframe")
    st.dataframe(df.head())

    #options for data cleaning
    st.subheader("Data Cleaning Options")
    if st.checkbox(f"clean Data for {file.name}"):
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates for {file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates removed")

        with col2:
            if st.button(f"fill missing values for {file.name}"):
               numeric_cols = df.select_dtypes(include=["numbers"]).columns
               df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
               st.write("Missing values filled")

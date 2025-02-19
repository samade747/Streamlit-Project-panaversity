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
    for file in uploaded_files:                       
        file_ext = os.path.splitext(file.name)[-1].lower()


    if file_ext == ".csv":
        df = pd.read_csv(file)
    elif file_ext == ".xlsx":
        df = pd.read_excel(file)
    else:
        st.error(f"Unsupported file type: {file_ext}")
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

        # choose specific colz to keep or convert
        st.subheader("Choose specific columns to keep or convert")
        columns = st.multiselect(f"choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]


        #Create some visualizations
        st.subheader("Data Visualizations")
        if st.checkbox(f"show visualizations for {file.name}"):
            st.bar_chart(df.select_dtypes(include="numbers").iloc[:,:2])

        #convert the file -> csv to excel
        st.subheader("Conversion Options")
        converstion_type = st.radio(f"choose conversion type for {file.name}", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name} "):
            buffer = BytesIO()
            if converstion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv") 
                min_type = "text/csv"         

            elif converstion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            #Download Button
            st.download_button(
                label=f"Download {file_name} as {converstion_type}",
                data=buffer,
                file_name=file_name,
                mime=mine_type
            )

    st.success(f"Successfully processed all files")
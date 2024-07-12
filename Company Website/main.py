import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("The Best Company")
st.write("TechCorp is a pioneering technology firm that develops and implements AI-powered solutions. Their innovative software and services cater to various industries, enhancing efficiency, productivity, and decision-making. With a strong focus on research and development, TechCorp strives to revolutionize businesses and transform lives through cutting-edge technology and expertise.")

st.header("Our Team")
df = pd.read_csv("data.csv")

col1, col2, col3, col4, col5 = st.columns([1, 0.5, 1, 0.5, 1])

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image("images/" + row["image"])
with col3:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image("images/" + row["image"])

with col5:
    for index, row in df[8:12].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"].title())
        st.image("images/" + row["image"])
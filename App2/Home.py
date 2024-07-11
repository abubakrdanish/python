import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

col1,empty_col, col2, = st.columns([2,1,2])
with col1:
    st.image("images/my.jpg", width=500)

with col2:
    st.title("Abubakar Danish")
    content = """
    Hello! I'm Abubakar, 23 years old, currently studying Computer Science at FAST University Karachi. I'm from Karachi and passionate about development skills. I enjoy exploring new technologies and finding creative solutions to challenges.
    """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3,empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pd.read_csv("data.csv",sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
import streamlit as st
import plotly.express as px
import pandas as pd
df = pd.read_csv("happy.csv")
st.title("In Search for happiness")

option1 = st.selectbox("Select the data for X-axis",("GDP","Happiness","Generosity"))
option2 = st.selectbox("Select the data for Y-axis",("GDP","Happiness","Generosity"))

st.subheader(f"{option1} and {option2}")
figure = px.scatter(x=df[option1.lower()], y=df[option2.lower()], labels={"x" : f"{option1}","y":f"{option2}"})
st.plotly_chart(figure)
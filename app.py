
import streamlit as st
import pandas as pd

st.title("🛒 E-Commerce Data Analysis")

data = pd.read_csv("your_data.csv")

st.subheader("Raw Dataset")
st.write(data.head())

st.subheader("Summary Statistics")
st.write(data.describe())

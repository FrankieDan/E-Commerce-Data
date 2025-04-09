# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.title("E-Commerce Data Analysis Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data successfully loaded!")

    # Display dataset
    if st.checkbox("Show raw data"):
        st.write(df)

    # Basic stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.subheader("Visualizations")
    column = st.selectbox("Select a column to visualize", df.select_dtypes(include='number').columns)

    st.write("Histogram")
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)

    st.write("Boxplot")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x=df[column], ax=ax2)
    st.pyplot(fig2)

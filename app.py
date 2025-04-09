
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("🛒 E-Commerce Data Analysis Dashboard")
st.markdown("Upload your CSV file to explore data, visualize trends, and review key metrics.")

uploaded_file = st.file_uploader("Upload your E-Commerce CSV data", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data loaded successfully!")

    # Show raw data
    with st.expander("📂 Show Raw Data"):
        st.dataframe(df, use_container_width=True)

    # KPIs
    st.subheader("📊 Key Performance Indicators (KPIs)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Orders", f"{df.shape[0]:,}")
    with col2:
        revenue_col = st.selectbox("Select Revenue Column", df.select_dtypes(include='number').columns, key="rev_kpi")
        st.metric("Total Revenue", f"${df[revenue_col].sum():,.2f}")
    with col3:
        st.metric("Average Order Value", f"${df[revenue_col].mean():.2f}")

    # Summary statistics
    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)

    # Numeric Visualizations
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        selected_num = st.selectbox("Select Numeric Column", numeric_cols)
        st.subheader(f"Histogram & Boxplot for {selected_num}")
        col4, col5 = st.columns(2)
        with col4:
            fig1, ax1 = plt.subplots()
            sns.histplot(df[selected_num], kde=True, ax=ax1)
            st.pyplot(fig1)
        with col5:
            fig2, ax2 = plt.subplots()
            sns.boxplot(x=df[selected_num], ax=ax2)
            st.pyplot(fig2)

    # Categorical Visualizations
    st.subheader("🧾 Categorical Data Insights")
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    if cat_cols:
        selected_cat = st.selectbox("Select Categorical Column", cat_cols)
        fig3, ax3 = plt.subplots()
        df[selected_cat].value_counts().plot(kind='bar', ax=ax3)
        ax3.set_title(f"Distribution of {selected_cat}")
        st.pyplot(fig3)

    # Correlation heatmap
    st.subheader("📌 Correlation Heatmap")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax4)
        st.pyplot(fig4)
    else:
        st.info("No numeric columns available for correlation analysis.")

else:
    st.info("Please upload a CSV file to get started.")

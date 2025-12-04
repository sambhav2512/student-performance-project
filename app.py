import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page configuration
st.set_page_config(page_title="Student Performance Analysis", layout="wide")

st.title("📊 Student Performance Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your student data CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Student Performance Table")
    st.dataframe(df)

    # Calculate Total & Average
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
    df["Average"] = df["Total"] / 3

    st.subheader("With Total & Average")
    st.dataframe(df)

    # --- Visualization 1: Bar Chart (Student Wise Total Marks)
    st.subheader("📈 Total Marks of Each Student")
    fig1, ax1 = plt.subplots(figsize=(8,5))
    sns.barplot(x="Name", y="Total", data=df, palette="viridis", ax=ax1)
    ax1.set_xlabel("Student Name")
    ax1.set_ylabel("Total Marks")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # --- Visualization 2: Subject Wise Comparison
    st.subheader("📊 Subject-wise Student Comparison")
    df_plot = df.melt(id_vars="Name", value_vars=["Math", "Science", "English"], 
                      var_name="Subject", value_name="Marks")
    fig2, ax2 = plt.subplots(figsize=(8,5))
    sns.lineplot(data=df_plot, x="Name", y="Marks", hue="Subject", marker="o", ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # --- Visualization 3: Heatmap for Subject Correlation
    st.subheader("🔥 Subject Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(6,4))
    sns.heatmap(df[["Math","Science","English"]].corr(), annot=True, cmap="coolwarm", ax=ax3)
    st.pyplot(fig3)

else:
    st.info("Please upload a CSV file to get started. Make sure it has columns: Name, Math, Science, English.")

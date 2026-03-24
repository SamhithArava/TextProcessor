import streamlit as st
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from rule_engine import analyze_chunk
from file_handler import split_into_chunks
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("🚀 Advanced Parallel Text Sentiment Analyzer")

# ---------------- QUICK ANALYZER ----------------
st.subheader("⚡ Quick Analyzer")

quick_text = st.text_area("Enter a sentence")

if st.button("Analyze Text"):
    if quick_text.strip() == "":
        st.warning("Please enter text")
    else:
        score, sentiment = analyze_chunk([quick_text])
        st.success(f"Sentiment: {sentiment} | Score: {score}")

st.divider()

# ---------------- FILE UPLOAD ----------------
st.subheader("📁 Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV / TXT / Excel", type=["csv", "txt", "xlsx"])

if uploaded_file:

    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            text = uploaded_file.read().decode("utf-8")
            df = pd.DataFrame({"text": text.split("\n")})

        st.write("🔍 Preview Data")
        st.dataframe(df.head())

        column = st.selectbox("Select Text Column", df.columns)

        data = df[column].dropna().astype(str).tolist()

        chunk_size = st.slider("Select Chunk Size", 100, 2000, 1000)

        chunks = split_into_chunks(data, int(chunk_size))

        if st.button("🚀 Process Data"):

            st.info("Processing...")

            # SINGLE
            start = time.time()
            single_results = [analyze_chunk(chunk) for chunk in chunks]
            single_time = time.time() - start

            # THREAD
            start = time.time()
            with ThreadPoolExecutor() as executor:
                thread_results = list(executor.map(analyze_chunk, chunks))
            thread_time = time.time() - start

            # PROCESS
            start = time.time()
            with Pool() as pool:
                process_results = pool.map(analyze_chunk, chunks)
            process_time = time.time() - start

            sentiments = []
            scores = []

            for chunk, result in zip(chunks, single_results):
                score, tag = result
                for line in chunk:
                    sentiments.append(tag)
                    scores.append(score)

            df["Sentiment"] = sentiments[:len(df)]
            df["Score"] = scores[:len(df)]

            # ---------------- DASHBOARD ----------------
            st.subheader("📊 Dashboard")

            positive_count = (df["Sentiment"] == "Positive").sum()
            negative_count = (df["Sentiment"] == "Negative").sum()
            neutral_count = (df["Sentiment"] == "Neutral").sum()
            total_score = df["Score"].sum()

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Records", len(df))
            col2.metric("Positive", positive_count)
            col3.metric("Negative", negative_count)
            col4.metric("Total Score", total_score)

            # BAR CHART
            st.subheader("📊 Sentiment Distribution (Bar Chart)")
            st.bar_chart(df["Sentiment"].value_counts())

            # PIE CHART
            st.subheader("🥧 Sentiment Distribution (Pie Chart)")
            pie_data = pd.DataFrame({
                "Sentiment": ["Positive", "Negative", "Neutral"],
                "Count": [positive_count, negative_count, neutral_count]
            })

            fig, ax = plt.subplots()
            ax.pie(pie_data["Count"], labels=pie_data["Sentiment"], autopct='%1.1f%%')
            ax.axis('equal')
            st.pyplot(fig)

            # ---------------- SEARCH ----------------
            st.subheader("🔍 Search")

            search = st.text_input("Enter keyword")

            if search:
                filtered = df[df[column].str.contains(search, case=False, na=False)]
                st.write(filtered)

            # ---------------- TOP RECORDS ----------------
            st.subheader("🏆 Top Positive & Negative Samples")

            st.write("Top Positive:")
            st.write(df[df["Sentiment"] == "Positive"].head())

            st.write("Top Negative:")
            st.write(df[df["Sentiment"] == "Negative"].head())

            # ---------------- PERFORMANCE ----------------
            st.subheader("⚡ Performance Analysis")

            st.write(f"Single Processing: {round(single_time,4)} sec")
            st.write(f"Thread Processing: {round(thread_time,4)} sec")
            st.write(f"Multiprocessing: {round(process_time,4)} sec")

            # ---------------- DOWNLOAD ----------------
            st.download_button("📥 Download Results", df.to_csv(index=False), "output.csv")

    except Exception as e:
        st.error(f"Error: {e}")
import streamlit as st
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
from rule_engine import analyze_chunk
from file_handler import split_into_chunks
import time

st.title("Parallel Text Sentiment Analyzer")

uploaded_file = st.file_uploader("Upload CSV / TXT / Excel", type=["csv", "txt", "xlsx"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")
        df = pd.DataFrame({"text": text.split("\n")})

    st.write(df.head())

    column = st.selectbox("Select Text Column", df.columns)

    data = df[column].dropna().tolist()

    chunk_size = st.number_input("Chunk Size", value=100)

    chunks = split_into_chunks(data, int(chunk_size))

    if st.button("Process Data"):

        start = time.time()
        single_results = [analyze_chunk(chunk) for chunk in chunks]
        single_time = time.time() - start

        start = time.time()
        with ThreadPoolExecutor() as executor:
            thread_results = list(executor.map(analyze_chunk, chunks))
        thread_time = time.time() - start

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

        st.subheader("Results")

        st.write("Total Records:", len(df))
        st.write(df["Sentiment"].value_counts())

        st.bar_chart(df["Sentiment"].value_counts())

        st.subheader("Performance")
        st.write("Single:", single_time)
        st.write("Thread:", thread_time)
        st.write("Multiprocessing:", process_time)

        search = st.text_input("Search Keyword")

        if search:
            filtered = df[df[column].str.contains(search, case=False, na=False)]
            st.write(filtered)

        st.download_button("Download CSV", df.to_csv(index=False), "output.csv")
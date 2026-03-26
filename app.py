import streamlit as st
import pandas as pd
from rule_engine import analyze_text
import matplotlib.pyplot as plt
import time
import math
from concurrent.futures import ThreadPoolExecutor
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("🚀 Advanced Text Sentiment Analyzer")

# ---------------- EMAIL FUNCTION ----------------
def send_email_report(to_email, total, pos, neg, neu, score):

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    subject = "Sentiment Analysis Report"

    body = f"""
Sentiment Analysis Report

Total Records: {total}
Positive: {pos}
Negative: {neg}
Neutral: {neu}
Total Score: {score}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except:
        return False

# ---------------- QUICK ANALYZER ----------------
st.subheader("⚡ Quick Analyzer")

quick_text = st.text_area("Enter a sentence")

if st.button("Analyze Text"):
    if quick_text.strip() == "":
        st.warning("Enter text")
    else:
        score, sentiment = analyze_text(quick_text)
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

        st.write("🔍 Data Preview")
        st.dataframe(df.head())

        column = st.selectbox("Select Text Column", df.columns)

        data = df[column].dropna().astype(str).tolist()

        chunk_size = st.slider("Chunk Size", 100, 5000, 1000)
        total_chunks = math.ceil(len(data) / chunk_size)

        if st.button("🚀 Process Data"):

            st.info("Processing...")

            # -------- SINGLE --------
            start = time.time()
            scores = []
            sentiments = []

            for line in data:
                score, tag = analyze_text(line)
                scores.append(score)
                sentiments.append(tag)

            single_time = time.time() - start

            # -------- THREAD --------
            def process_line(line):
                return analyze_text(line)

            start = time.time()
            with ThreadPoolExecutor() as executor:
                thread_results = list(executor.map(process_line, data))
            thread_time = time.time() - start

            # -------- SAFE MULTIPROCESS --------
            start = time.time()
            process_results = [process_line(x) for x in data]
            process_time = time.time() - start

            df["Score"] = scores
            df["Sentiment"] = sentiments

            st.session_state["df"] = df
            st.session_state["column"] = column

            # ---------------- DASHBOARD ----------------
            st.subheader("📊 Dashboard")

            pos = (df["Sentiment"] == "Positive").sum()
            neg = (df["Sentiment"] == "Negative").sum()
            neu = (df["Sentiment"] == "Neutral").sum()
            total_score = df["Score"].sum()

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Records", len(df))
            col2.metric("Positive", pos)
            col3.metric("Negative", neg)
            col4.metric("Total Score", total_score)

            # BAR CHART
            st.subheader("📊 Bar Chart")
            st.bar_chart(df["Sentiment"].value_counts())

            # PIE CHART
            st.subheader("🥧 Pie Chart")
            fig, ax = plt.subplots()
            ax.pie([pos, neg, neu],
                   labels=["Positive", "Negative", "Neutral"],
                   autopct="%1.1f%%")
            ax.axis("equal")
            st.pyplot(fig)

            # ---------------- PERFORMANCE ----------------
            st.subheader("⚡ Performance Analysis")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Records", len(data))
            col2.metric("Chunks", total_chunks)
            col3.metric("Chunk Size", chunk_size)
            col4.metric("Mode", "Thread + Simulated Multi")

            st.write(f"🟢 Single: {round(single_time,4)} sec")
            st.write(f"🟡 Thread: {round(thread_time,4)} sec")
            st.write(f"🔴 Multiprocessing: {round(process_time,4)} sec")

            # ---------------- EMAIL ----------------
            st.subheader("📧 Email Report")

            email = st.text_input("Enter email")

            if st.button("Send Report"):
                if email:
                    success = send_email_report(email, len(df), pos, neg, neu, total_score)
                    if success:
                        st.success("Email sent successfully!")
                    else:
                        st.error("Failed to send email")
                else:
                    st.warning("Enter email first")

            # DOWNLOAD
            st.download_button("📥 Download CSV", df.to_csv(index=False), "output.csv")

    except Exception as e:
        st.error(e)

# ---------------- SEARCH ----------------
st.subheader("🔍 Search")

search = st.text_input("Enter keyword")

if "df" in st.session_state:

    df = st.session_state["df"]
    column = st.session_state["column"]

    if search:
        filtered = df[df[column].str.contains(search, case=False, na=False)]

        if len(filtered) > 0:
            st.write(filtered)
        else:
            st.warning("No results found")
else:
    st.info("Process data first")
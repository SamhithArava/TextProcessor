# 🚀 Parallel Text Sentiment Analyzer

## 📌 Project Overview
This project is a web-based sentiment analysis system designed to process large-scale text datasets efficiently. It allows users to upload files, analyze textual data using rule-based sentiment scoring, and visualize results through interactive dashboards.

The system also demonstrates the concept of parallel processing by comparing execution performance between sequential and parallel approaches.

---

## 🎯 Objective
The main objective of this project is to:
- Analyze large volumes of text data
- Classify sentiment into Positive, Negative, and Neutral
- Improve performance using parallel processing
- Provide a user-friendly interface for data interaction

---

## ✨ Features Implemented

### 📁 File Upload
- Supports CSV, TXT, and Excel files
- Handles large datasets (50,000+ records)

### ⚡ Quick Analyzer
- Analyze individual sentences instantly
- Useful for testing sentiment logic

### 🔍 Search Functionality
- Allows users to search specific keywords
- Filters matching records dynamically

### 📊 Dashboard
Displays:
- Total number of records
- Positive count
- Negative count
- Neutral count
- Total sentiment score

### 📈 Visualization
- Bar chart for sentiment distribution
- Pie chart for percentage representation

### 📥 Export Feature
- Download processed results as CSV file

### ⚡ Performance Analysis
- Compares execution time for:
  - Sequential processing
  - Multithreading
  - Simulated multiprocessing
- Displays chunk size and number of chunks

---

## 🧠 Sentiment Analysis Logic

The system uses a rule-based approach:

### Positive Words
```
good, excellent, amazing, great, happy
```

### Negative Words
```
bad, terrible, worst, poor, boring, difficult
```

### Scoring Method
- Each positive word → +1
- Each negative word → -1
- Final Score = Positive count - Negative count

### Special Cases Handled
- **"not good"** → considered negative
- **"very good"** → strong positive
- Repeated words are counted multiple times

### Example:
```
Input: good good bad
Score: +1 +1 -1 = +1 → Positive
```

---

## ⚙️ Parallel Processing Logic

The system compares three processing methods:

### 1. Sequential Processing
- Processes data line by line
- Simple but slower for large datasets

### 2. Multithreading
- Uses ThreadPoolExecutor
- Faster for I/O-bound tasks

### 3. Multiprocessing (Simulated)
- Designed to demonstrate multi-core execution
- In Streamlit, true multiprocessing can cause instability
- Hence a safe simulation approach is used

### Key Concept:
- Parallel processing improves performance for large datasets
- Overhead may make it slower for small datasets

---

## 📊 Dataset Details

- Dataset consists of student feedback
- Generated programmatically
- Includes:
  - Positive sentences
  - Negative sentences
  - Neutral sentences
  - Mixed and repeated word cases

### Example:
```
The teaching was excellent and helpful
The experience was bad and boring
good good bad explanation
not good teaching method
```

---

## ⚡ Performance Comparison

| Method          | Behavior |
|----------------|--------|
| Sequential     | Simple but slower |
| Threading      | Moderate speed improvement |
| Multiprocessing| Best for CPU-heavy tasks |

### Observation:
- For small datasets → Sequential may be faster
- For large datasets → Parallel processing performs better

---

## ⚠️ Edge Cases Handled

- Empty input file
- Invalid file format
- Missing text column
- Large dataset handling (50K+ records)
- Repeated words
- Special phrases ("not good", "very good")
- Case-insensitive search

---

## 🏗️ Project Structure

```
TextProcessor/
│── app.py
│── rule_engine.py
│── file_handler.py
│── requirements.txt
│── README.md
│── LICENSE
│── agile.md
```

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies
```
pip install -r requirements.txt
```

### Step 2: Run Application
```
streamlit run app.py
```

### Step 3: Open Browser
```
http://localhost:8501
```

---

## 📌 Agile Documentation

The project was developed incrementally with:
- Daily progress tracking
- Feature-based implementation
- Continuous improvements and bug fixing

---

## 📜 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author
Samhith Arava

---

## 💡 Final Note
This project demonstrates both functional implementation and performance analysis, making it a complete end-to-end system for large-scale text processing and sentiment evaluation.
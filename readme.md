Python Parallel Text Processing System
Milestone 2 – Performance, Scalability, and Optimization
1. Project Overview
This project implements a scalable text processing pipeline using Python. The system is designed to process large volumes of textual data efficiently using parallel execution techniques and rule-based sentiment analysis.

Milestone 1 focused on building a working pipeline.
Milestone 2 focuses on improving performance, benchmarking execution models, testing scalability, and optimizing database operations.

2. System Architecture
The system follows a structured processing pipeline:

Input File
   ↓
Chunk Segmentation
   ↓
Processing (Single / Threading / Multiprocessing)
   ↓
Weighted Sentiment Evaluation
   ↓
Bulk Database Insert
   ↓
Indexed Query Execution
   ↓
Performance Reporting
3. Project Structure
TextProcessor/
│
├── main.py               # Core pipeline controller
├── file_handler.py       # File reading and chunk logic
├── rule_engine.py        # Weighted sentiment scoring engine
├── database.py           # SQLite integration & optimization
├── generate_input.py     # Scalable dataset generator
├── input.txt             # Input dataset
├── text_results.db       # SQLite database
├── .gitignore
└── README.md
4. Weighted Rule-Based Sentiment Engine
Milestone 2 replaces simple counting with weighted scoring.

Positive Rules
"excellent": +3
"amazing": +2
"good": +1
"happy": +2
Negative Rules
"terrible": -3
"bad": -1
"worst": -2
"error": -2
Scoring Formula
Final Score = Sum of matched word weights
Classification
Score > 0 → Positive

Score < 0 → Negative

Score = 0 → Neutral

This allows more expressive and realistic sentiment evaluation.

5. Parallel Processing Benchmarking
The system compares three execution models:

1. Single Processing
Standard for-loop execution.

2. ThreadPoolExecutor
Uses multiple threads for concurrent execution.

3. Multiprocessing Pool
Uses separate processes for true parallel execution.

Performance Measurement
Execution time is recorded using:

time.time()
Example Output:

Single Processing Time: 4.82 seconds
ThreadPool Time: 4.11 seconds
Multiprocessing Time: 2.35 seconds
6. CPU-Bound vs I/O-Bound Analysis
This workload is CPU-bound because:

Sentiment scoring involves repeated computation

Word matching operations dominate execution

Minimal waiting on file or network I/O

Multiprocessing performs better due to Python's Global Interpreter Lock (GIL), which restricts true parallelism in threading for CPU-bound tasks.

7. Scalability Testing
The system was tested with increasing dataset sizes:

100 reviews

10,000 reviews

100,000 reviews

For each dataset, the following metrics were recorded:

Processing time

Bulk insert time

Query time

Performance growth was analyzed to observe scalability patterns.

8. Database Optimization
Milestone 2 introduces two major optimizations:

1. Bulk Insert using executemany()
Instead of inserting row-by-row, all processed data is inserted in a single transaction.
This significantly reduces commit overhead.

2. Index Creation
CREATE INDEX idx_sentiment ON text_results(sentiment);
This improves filtering queries on sentiment.

Query Benchmark
Query time before and after indexing shows measurable improvement, especially for large datasets.

9. Performance Components Measured
The system records:

Single Processing Time

ThreadPool Time

Multiprocessing Time

Bulk Insert Time

Indexed Query Time

This provides full visibility into computational and database overhead.

10. How to Run
Step 1 – Generate Dataset
python generate_input.py
Enter desired number of reviews.

Step 2 – Execute Pipeline
python main.py
Enter chunk size when prompted.

11. Key Learnings from Milestone 2
Weighted rule systems provide more realistic scoring.

Multiprocessing improves CPU-bound workload performance.

Threading may not outperform single execution due to GIL.

Bulk insertion drastically improves database write speed.

Indexing significantly reduces query time.

Scalability testing reveals non-linear growth patterns.

12. Future Improvements
Replace rule engine with NLP model

Add REST API layer

Add visualization dashboard

Introduce caching layer

Implement distributed processing

13. Author
Samhith Arava


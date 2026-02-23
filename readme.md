Parallel Text Processing System with Rule-Based Sentiment Analysis
Abstract
This project presents a modular text processing system designed to efficiently handle large textual datasets using parallel execution techniques in Python. The system implements chunk-based processing, rule-based sentiment evaluation, structured database storage, and execution time measurement. The architecture emphasizes modularity, scalability, and clarity of implementation.

Problem Statement
Processing large text files sequentially can lead to performance bottlenecks. The objective of this project is to design a structured processing pipeline that:

Segments large datasets into manageable chunks

Executes chunk processing concurrently

Applies deterministic sentiment scoring

Stores results in a relational database

Measures execution performance

System Architecture
The system follows a layered processing model:

Input File
   ↓
Text Segmentation (Chunking)
   ↓
Parallel Execution
   ↓
Rule-Based Sentiment Evaluation
   ↓
SQLite Database Storage
   ↓
Execution Summary
Design Principles
Modular separation of concerns

Clean function-level abstraction

Parallel computation using thread pools

Lightweight database integration

Deterministic rule-based evaluation

Implementation Details
1. File Handling and Chunking
Large text files are read into memory and segmented into fixed-size chunks using range-based slicing:

Ensures scalability

Enables distributed execution

Maintains manageable processing units

2. Parallel Processing
Parallel execution is implemented using:

ThreadPoolExecutor
Each chunk is assigned to a worker thread where sentiment evaluation is performed concurrently. This reduces overall processing time compared to sequential iteration.

3. Rule-Based Sentiment Engine
Sentiment scoring follows a deterministic model:

score = positive_count - negative_count
Classification logic:

Score > 0 → Positive

Score < 0 → Negative

Score = 0 → Neutral

This approach avoids external dependencies and maintains full transparency of scoring logic.

4. Database Integration
SQLite is used as a lightweight relational storage system.

Each processed chunk is stored with:

Chunk Text

Sentiment Score

Sentiment Label

The database schema ensures structured and persistent storage of processed results.

5. Execution Time Measurement
Total runtime is measured using Python’s time module to evaluate performance characteristics of the parallel implementation.

Project Structure
TextProcessor/
│
├── main.py
├── file_handler.py
├── rule_engine.py
├── database.py
├── generate_input.py
├── input.txt
├── .gitignore
└── README.md
How to Execute
Run the main pipeline:

python main.py
To generate sample input:

python generate_input.py
Evaluation Focus
This implementation demonstrates:

Practical use of concurrency in Python

Structured modular design

Clean database integration

Deterministic text analysis logic

Performance monitoring

Scope for Enhancement
Search and filtering functionality

CSV export capability

API layer for external access

User interface integration

Advanced NLP model integration

Author
Samhith Arava
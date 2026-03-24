import sqlite3
import time

def create_database():
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS text_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chunk TEXT,
        score INTEGER,
        sentiment TEXT
    )
    """)

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON text_results(sentiment)")

    conn.commit()
    conn.close()


def bulk_insert(data):
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO text_results (chunk, score, sentiment) VALUES (?, ?, ?)",
        data
    )

    conn.commit()
    conn.close()


def test_query():
    conn = sqlite3.connect("text_results.db")
    cursor = conn.cursor()

    start = time.time()
    cursor.execute("SELECT * FROM text_results WHERE sentiment='Positive'")
    cursor.fetchall()
    end = time.time()

    conn.close()
    return end - start
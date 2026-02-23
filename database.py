import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS text_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chunk TEXT,
        score INTEGER,
        sentiment TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_result(chunk_text, score, sentiment):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO text_results (chunk, score, sentiment)
    VALUES (?, ?, ?)
    """, (chunk_text, score, sentiment))

    conn.commit()
    conn.close()
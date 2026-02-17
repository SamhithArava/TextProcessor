import sqlite3

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        branch TEXT,
        marks INTEGER
    )
    """)

    students_data = [
        ("Sam", "CSE", 85),
        ("Ravi", "ECE", 78),
        ("Anu", "CSE", 92),
        ("Priya", "EEE", 88),
        ("Kiran", "MECH", 74)
    ]

    cursor.executemany(
        "INSERT INTO students (name, branch, marks) VALUES (?, ?, ?)",
        students_data
    )

    conn.commit()
    conn.close()
    print("Database created and 5 records inserted.")

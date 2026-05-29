import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "school.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute(""" --begin-sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT
)
""")


conn.commit()
conn.close()

print("Table created successfully")

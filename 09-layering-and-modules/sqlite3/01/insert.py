import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "school.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

name = "Sara"
age = 22
major = "Math"

cursor.execute(
    """
                INSERT INTO students (name, age, major)
                VALUES (?,?,?)
               """,
    (name, age, major),
)

conn.commit()
conn.close()

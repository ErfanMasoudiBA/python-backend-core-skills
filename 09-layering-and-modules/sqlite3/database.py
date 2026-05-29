import os
import sqlite3
from contextlib import contextmanager

Base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(Base_dir, "school.db")


@contextmanager
def get_db_connection():
    conn = sqlite3.connect(db_path)
    try:
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Database error: {e}")
        raise e
    finally:
        conn.close()

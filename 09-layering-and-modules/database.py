import os
import sqlite3
from contextlib import contextmanager

Base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(Base_dir, "bank.db")


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


def create_tables():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        sql_query = """ --begin-sql
            CREATE TABLE IF NOT EXISTS accounts (
                owner TEXT PRIMARY KEY,
                balance INTEGER
            )
            --end-sql
        """
        cursor.execute(sql_query)
        print("Table created successfully.")


if __name__ == "__main__":
    create_tables()

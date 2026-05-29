from database import get_db_connection


def create_tables():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """ --begin-sql
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                major TEXT
            )
            --end-sql
            """
        )
        print("Table created successfully.")


if __name__ == "__main__":
    create_tables()

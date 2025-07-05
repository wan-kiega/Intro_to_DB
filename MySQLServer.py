import mysql.connector
from mysql.connector import errorcode

def create_database(db_name: str, host: str, user: str, password: str) -> None:
    conn = None
    cursor = None

    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS alx_book_store "
            "DEFAULT CHARACTER SET utf8mb4"
        )
        print(f"Database `{db_name}` created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied: check username or password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Unknown database!")
        else:
            print(f"MySQL Error: {err}")
    except Exception as exc:
        print(f"Unexpected error: {exc}")
    finally:
        if cursor is not None:
            cursor.close()
            print("Cursor closed.")
        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection closed.")

# Entry point
if __name__ == "__main__":
    create_database(
        db_name="alx_book_store",
        host="localhost",
        user="root",
        password="password"
    )

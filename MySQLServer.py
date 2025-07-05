import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',
            user='Local instance MySQL80',  # Replace with your MySQL username
            password='WanjiruKiega@001'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor.is_connected():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
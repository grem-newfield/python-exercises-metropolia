import sqlite3
import csv


def test_database_operations():
    # Connect to the SQLite database
    conn = sqlite3.connect(
        database="airports",
    )
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)"
    )

    # Insert a record
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        ("user1", "user1@example.com"),
    )
    conn.commit()

    # Fetch data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Clean up
    conn.close()

    # Assertion for testing
    assert len(rows) == 1
    assert rows[0][1] == "user1"

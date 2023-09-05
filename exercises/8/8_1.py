# 8. Using relational databases
import sqlite3
import csv

# 1. Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and
# location (town) from the airport database used on this course. The ICAO codes
# are stored in the ident column of the airport table.

import mariadb

conn = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    database="airports",
    user="grem",
    password="",
    autocommit=True,
)


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

# 8. Using relational databases
import sqlite3
import csv

# 1. Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and
# location (town) from the airport database used on this course. The ICAO codes
# are stored in the ident column of the airport table.

import mariadb


def test_database_operations():
    conn = mariadb.connect(
        host="127.0.0.1",
        port=3306,
        database="",
        user="grem",
        # password=None,
        autocommit=True,
    )
    cursor = conn.cursor()
    # Fetch data
    cursor.execute("select * from airports limit 1")
    rows = cursor.fetchall()
    print(rows)
    # Clean up
    conn.close()

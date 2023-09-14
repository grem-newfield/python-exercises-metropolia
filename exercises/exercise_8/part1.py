# . Using relational databases

# 1. Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and
# location (town) from the airport database used on this course. The ICAO codes
# are stored in the ident column of the airport table.

import mysql.connector
from helpers import asker


def part1():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            database="test",
            user="db_user",
            password="thereisaspoon",
            autocommit=True,
        )
    except Exception:
        print("Cant reach the database.")
        return

    def get_airport_by_icao(icao):
        sql = "SELECT name, municipality "
        sql += f'FROM airport WHERE ident = "{icao}"'
        print("Query:")
        print(sql, "\n")
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                print(f"Airport: {row[0]}, located in {row[1]}")
        conn.close()
        return

    icao = asker("Type the ICAO code: ", "string").upper()
    print()
    get_airport_by_icao(icao)


if __name__ == "__main__":
    part1()

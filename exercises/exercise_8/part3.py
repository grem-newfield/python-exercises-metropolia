# 3. Write a program that asks the user to enter the ICAO codes of two
# airports. The program prints out the distance between the two airports in
# kilometers. The calculation is based on the airport coordinates fetched from
# the database. Calculate the distance using the `geopy` library:
# https://geopy.readthedocs.io/en/stable/. Install the library by selecting
# **View / Tool Windows / Python Packages** in your PyCharm IDE, write `geopy`
# into the search field and finish the installation.

from typing import Any, Tuple
from helpers import asker
import mysql.connector
from geopy.distance import geodesic


def part3():
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

    def get_airport_by_icao(icao) -> Tuple[Any, Any, Any]:
        # we open a new connection every time, oof
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
            exit()
        sql = "SELECT name, latitude_deg, longitude_deg "
        sql += f'FROM airport WHERE ident = "{icao}"'
        print("Query:")
        print(sql, "\n")
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # if cursor.rowcount > 0:
        #     for row in result:
        #         print(f"Airport: {row[0]}, located in {row[1]}")
        conn.close()
        try:
            return (result[0][0], result[0][1], result[0][2])
        except Exception:
            print("Please input valid ICAO's")
            exit()

    icao = asker("Type the first airports ICAO code: ", "string").upper()
    print()
    airport_1, airport_1_latitude, airport_1_longitude = get_airport_by_icao(icao)
    icao = asker("Type the second airports ICAO code: ", "string").upper()
    print()
    airport_2, airport_2_latitude, airport_2_longitude = get_airport_by_icao(icao)

    print(airport_1)
    print(airport_2)

    dist = geodesic(
        (airport_1_latitude, airport_1_longitude),
        (airport_2_latitude, airport_2_longitude),
    ).kilometers

    print(f"Distance between them is {dist:0.2f} km.")


if __name__ == "__main__":
    part3()

# 2. Write a program that asks the user to enter the area code (for example
# `FI`) and
# prints out the airports located in that country ordered by airport type. For
# example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector
from helpers import asker


def part2():
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

    def get_airports_by_country_code(cc):
        sql = f"""
        SELECT
          airport.name, airport.type, country.name
        FROM
          country, airport
        WHERE
          country.iso_country = "{cc}" AND
          airport.iso_country = country.iso_country
        ORDER BY
          airport.type """

        print("Query:")
        print(sql, "\n")
        (closed, large, small, medium) = 0, 0, 0, 0

        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Airports:")
        if cursor.rowcount > 0:
            for row in result:
                match row[1]:
                    case "closed":
                        closed += 1
                    case "large_airport":
                        large += 1
                    case "small_airport":
                        small += 1
                    case "medium_airport":
                        medium += 1
                print(f"Type: {row[1]} Name: {row[0]}")

        print(f"In {result[0][2]} there are:")  # cursed name get
        print(f"{large} large airports")
        print(f"{medium} medium airports")
        print(f"{small} small airports")
        print(f"{closed} closed airports")

        conn.close()
        return

    country_code = asker("Type the country code: ", "string").upper()
    print()
    get_airports_by_country_code(country_code)


if __name__ == "__main__":
    part2()

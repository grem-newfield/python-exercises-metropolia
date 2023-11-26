from flask import Flask, url_for
import json
import mysql.connector

app = Flask(__name__)


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print("\t", f)
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


# 1. Implement a Flask backend service that tells whether a number received as
# a parameter is a prime number or not. Use the prior prime number exercise as
# a starting point.

# For example, a GET request for number 31 is given as:
# `http://127.0.0.1:5000/prime_number/31`.

# The response must be in the format of
# `{"Number":31, "isPrime":true}`.


@app.route("/prime_number/<num>")
def prime_number(num):
    num = int(num)
    # return f" {is_prime(num)}"
    return json.dumps({"Number": num, "isPrime": is_prime(num)})


# returns the name and location of the airport in JSON format. The information
# is fetched from the airport database used on this course. For example, the
# GET request for EFHK would be: `http://127.0.0.1:5000/airport/EFHK`. The
# response must be in the format of: `{"ICAO":"EFHK", "Name":"Helsinki-Vantaa
# Airport", "Location":"Helsinki"}`.


@app.route("/airport/<icao>")
def airport(icao):
    result = json.dumps({"Error": "Undefined"})
    try:
        connection = mysql.connector.connect(
            user="db_user", password="thereisaspoon", host="127.0.0.1", database="test"
        )
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT ident, name, municipality FROM airport WHERE ident = "{icao}"'
        )
        result = cursor.fetchall()[0]  # first line
    finally:
        connection.close()
    return json.dumps({"ICAO": result[0], "Name": result[1], "Location": result[2]})

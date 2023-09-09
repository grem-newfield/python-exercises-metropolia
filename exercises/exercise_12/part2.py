# 2. Familiarize yourself with the OpenWeather weather API at:
# https://openweathermap.org/api. Your task is to write a program that asks the
# user for the name of a municipality and then prints out the corresponding
# weather condition description text and temperature in Celsius degrees. Take a
# good look at the API documentation. You must register for the service to
# receive the API key required for making API requests. Furthermore, find out
# how you can convert Kelvin degrees into Celsius.

import requests
import json

API_key = "f3bb229f79f2b6ead7aafa3241262b80"


def part2():
    get_weather("s", "s", API_key)


def get_weather(municipality_name, country_code, API_key):
    try:
        # answer = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}').json()
        answer = requests.get(
            f"https://api.openweathermap.org/data/3.0/onecall?q=Helsinki,FI&appid={API_key}"
        ).json()
        print(answer)
    except:
        print("Couldn't fetch joke catergories")
        return


if __name__ == "__main__":
    part2()

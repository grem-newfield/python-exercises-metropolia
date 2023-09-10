import requests
import json


def part2():
    # Exposed API Key btw, nice
    API_key = "f3bb229f79f2b6ead7aafa3241262b80"

    def get_weather_request(municipality_name):
        answer = "unset"
        try:
            answer = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={municipality_name}&appid={API_key}"
            ).content
            return answer
        except:
            print("ERROR")
            return answer

    while True:
        try:
            municipality_name = input("Choose a municipality: ").strip()
            break
        except KeyboardInterrupt:
            exit()
        except:
            print("Couldnt parse the name")
            continue
    raw = get_weather_request(municipality_name)
    raw = json.loads(raw)
    if raw["cod"] == 200:
        print(f"Current weather in {municipality_name}, {raw['sys']['country']} :")
        print(
            f"Condition: {raw['weather'][0]['main']}, {raw['weather'][0]['description']}"
        )
        print(f"Temperature: {(raw['main']['temp'] - 273.15):.2f} C")
    else:
        print("Server response: ", raw["message"])


# {
# 'coord': {'lon': 37.6156, 'lat': 55.7522},
# 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}],
# 'base': 'stations',
# 'main':
#     {'temp': 284.14, 'feels_like': 283.15, 'temp_min': 282.9, 'temp_max': 285.58, 'pressure': 1023, 'humidity': 71, 'sea_level': 1023, 'grnd_level': 1005},
# 'visibility': 10000,
# 'wind': {'speed': 3.63, 'deg': 346, 'gust': 7.53},
# 'clouds': {'all': 82},
# 'dt': 1694301876,
# 'sys': {'type': 2, 'id': 2000314, 'country': 'RU', 'sunrise': 1694314248, 'sunset': 1694361779},
# 'timezone': 10800,
# 'id': 524901,
# 'name': 'Moscow',
# 'cod': 200
# }


if __name__ == "__main__":
    part2()

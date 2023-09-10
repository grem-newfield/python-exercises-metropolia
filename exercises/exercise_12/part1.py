from random import choice
import requests
import json


def part1():
    try:
        catergories = requests.get("https://api.chucknorris.io/jokes/categories").json()
        # print(catergories)
    except:
        print("Couldn't fetch joke catergories")
        return
    random_catergory = choice(catergories)
    try:
        joke = json.loads(
            requests.get(
                f"https://api.chucknorris.io/jokes/random?category={random_catergory}"
            ).content
        )["value"]
        print(joke)
    except:
        print("Couldn't fetch joke")
        return


if __name__ == "__main__":
    part1()

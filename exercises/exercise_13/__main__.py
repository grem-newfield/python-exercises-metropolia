# 13. Setting up a backend service with an interface
from sys import argv
from subprocess import Popen
import time
import requests
import os


def break_line():
    print("-" * 80)
    print()


def part1():
    backend = Popen(
        ["flask -A app run"],
        shell=True,
        cwd=os.path.dirname(os.path.realpath(__file__)),
    )
    num = 31
    time.sleep(1)
    break_line()
    while True:
        try:
            num = int(input("Give me a number: (int) "))
            break
        except KeyboardInterrupt:
            break
        except Exception:
            print("Invalid input")
            continue
    resp = requests.get(f"http://127.0.0.1:5000/prime_number/{num}").json()
    print(resp)
    backend.terminate()


def part2():
    try:
        backend = Popen(
            ["flask -A app run"],
            shell=True,
            cwd=os.path.dirname(os.path.realpath(__file__)),
        )
        icao = "EFHK"
        time.sleep(1)
        break_line()
        while True:
            try:
                icao = input("Input airport ICAO: ").upper()
                break
            except KeyboardInterrupt:
                break
            except Exception:
                print("Invalid input")
                continue
        resp = requests.get(f"http://127.0.0.1:5000/airport/{icao}").json()
        print(resp)
        backend.terminate()
    except Exception:
        try:
            backend.terminate()
        except Exception:
            pass
        print("An Error has occured.")
        print("Exiting...")
        return


choice = "all"
try:
    if argv[1]:
        choice = str(argv[1])
except Exception:
    print(
        """Hint: you can pass your choice as an argument
to the script like: python 6.py 4\n"""
    )
    choice = str(input("Hello, what part of the 13th exercise?\n(1,2,all): "))

match choice:
    case "1":
        part1()
        break_line()
    case "2":
        part2()
        break_line()
    case "all":
        part1()
        break_line()
        part2()
        break_line()
    case _:
        print("Wrong input?\nExiting...")

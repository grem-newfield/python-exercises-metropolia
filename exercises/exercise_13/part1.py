# 1. Implement a Flask backend service that tells whether a number received as
# a parameter is a prime number or not. Use the prior prime number exercise as
# a starting point. For example, a GET request for number 31 is given as:
# `http://127.0.0.1:5000/prime_number/31`. The response must be in the format
# of `{"Number":31, "isPrime":true}`.

import os
import platform

if platform.system() == "Linux":
    os.spawnv(os.P_NOWAIT, "ls", ["-l"])
if platform.system() == "Windows":
    os.spawnv(os.P_NOWAIT, "lmao", [])
if platform.system() == "Darwin":
    print("I have no will to build for Apple devices")
if platform.system() == "Java":
    print("What")


def part1():
    pass


if __name__ == "__main__":
    part1()

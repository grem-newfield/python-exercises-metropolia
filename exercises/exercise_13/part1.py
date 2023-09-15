# 1. Implement a Flask backend service that tells whether a number received as
# a parameter is a prime number or not. Use the prior prime number exercise as
# a starting point.

# For example, a GET request for number 31 is given as:
# `http://127.0.0.1:5000/prime_number/31`.

# The response must be in the format of
# `{"Number":31, "isPrime":true}`.


def part1():
    from subprocess import Popen
    import platform
    import requests
    import os

    match platform.system():
        case "Linux":
            try:
                backend = Popen(
                    ["./backend_service"],
                    shell=True,
                    cwd=os.path.dirname(os.path.realpath(__file__)),
                )
                num = 31
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
            except Exception:
                print("Something went wrong :(")
            try:
                backend.terminate()
            except Exception:
                return
        case "Windows":
            print(
                """
Unfortunately you are running an inferior operating system,
you will have to install Rust programming language and
build the backend_service_rs app from source yourself:
# cd backend_service_rs/
# cargo run --release
"""
            )
            match input("Did you run the backend_service? (y/n) "):
                case "y" | "yes":
                    num = 31
                    while True:
                        try:
                            num = int(input("Give me a number: (int) "))
                            break
                        except KeyboardInterrupt:
                            break
                        except Exception:
                            print("Invalid input")
                            continue
                    resp = requests.get(
                        f"http://127.0.0.1:5000/prime_number/{num}"
                    ).json()
                    print(resp)
                case _:
                    print("Exiting...")
        case "Darwin":
            print("I have no will to build for Apple.")
        case _:
            print("What")


if __name__ == "__main__":
    part1()

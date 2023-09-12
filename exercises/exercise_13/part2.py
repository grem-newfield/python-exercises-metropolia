# returns the name and location of the airport in JSON format. The information
# is fetched from the airport database used on this course. For example, the
# GET request for EFHK would be: `http://127.0.0.1:5000/airport/EFHK`. The
# response must be in the format of: `{"ICAO":"EFHK", "Name":"Helsinki-Vantaa
# Airport", "Location":"Helsinki"}`.


def part2():
    from subprocess import Popen
    import platform
    import requests

    match platform.system():
        case "Linux":
            try:
                backend = Popen(["./backend_service"], shell=True)
                icao = "EFHK"
                while True:
                    try:
                        icao = input("Input airport ICAO: ").upper()
                        break
                    except KeyboardInterrupt:
                        break
                    except:
                        print("Invalid input")
                        continue
                # TODO:Implement airport database query in backend_service
                resp = requests.get("http://127.0.0.1:5000/airport/{icao}").json()
                print(resp)
            except:
                print("Something went wrong :(")
            try:
                backend.terminate()
            except:
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
                    icao = "EFHK"
                    while True:
                        try:
                            icao = input("Input airport ICAO: ").upper()
                            break
                        except KeyboardInterrupt:
                            break
                        except:
                            print("Invalid input")
                            continue
                    resp = requests.get("http://127.0.0.1:5000/airport/{icao}").json()
                    print(resp)
                case _:
                    print("Exiting...")
        case "Darwin":
            print("I have no will to build for Apple.")
        case _:
            print("What")


if __name__ == "__main__":
    part2()

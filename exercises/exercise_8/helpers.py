def break_line():
    print("-" * 80)
    print()


def asker(prompt, t):
    while True:
        try:
            match t:
                case "float":
                    return float(input(prompt).strip())
                case "int":
                    return int(input(prompt).strip())
                case "string":
                    return input(prompt).strip()
                case "list":
                    return input(prompt).strip().split(" ")
                case _:
                    return
        except KeyboardInterrupt:
            exit()
        except Exception:
            match t:
                case "float" | "int":
                    print("NaN")
                case _:
                    print("Invalid input")
            continue

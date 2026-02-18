def garden_operations(x: any, y: int) -> None:
    if y == 1:
        try:
            open(x, "r")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
    elif y == 2:
        try:
            print(int(x))
        except ValueError as e:
            print(f"Caught ValueError: {e}")
    elif y == 3:
        try:
            x /= 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
    elif y == 4:
        try:
            x['ahmed']
        except KeyError as e:
            print(f"Caught KeyError: {e}")
    else:
        try:
            x = 'abc'
            print(int(x))
            open(x, "r")
        except (FileNotFoundError, ValueError):
            print("Caught an error, the program continues..")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing FileNotFoundError..")
    garden_operations('abc', 1)
    print()
    print("Testing ValueError..")
    garden_operations('abc', 2)
    print()
    print("Testing ZeroDivisionError..")
    garden_operations(5, 3)
    print()
    print("Testing KeyError..")
    garden_operations({'soso': 'banana'}, 4)
    print()
    print("Testing multiple errors together...")
    garden_operations(98, 99)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

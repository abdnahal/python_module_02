def garden_operations(x, y):
    if y == 1:
        try:
            open(x, "r")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'test.txt'")
    elif y == 2:
        try:
            print(int(x))
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif y == 3:
        try:
            x /= 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif y == 4:
        try:
            x['ahmed']
        except KeyError:
            print("Caught KeyError: 'ahmed'")
    else:
        try:
            x = 'abc'
            print(int(x))
            open(x, "r")
        except (FileNotFoundError, ValueError):
            print("Caught an error, the program continues..")


def test_error_types():
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

def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
        elif temp < 0:
            print(f"Temperature {temp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp}°C is too hot for plants (max 40°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input():
    temp_str = input("Testing temperature: ")
    test_cases = ['25', 'abc', '100', '-50']
    check_temperature(temp_str)
    for case in test_cases:
        print(f"Testing temperature: {case}")
        check_temperature(case)
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()

def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp < 0:
            print(f"Temperature {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    temp_str = input("Testing temperature: ")
    check_temperature(temp_str)


def main():
    test_temperature_input()


if __name__ == "__main__":
    main()
def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif sunlight_hours > 12:
            raise ValueError(f"{sunlight_hours} hours is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(f"{sunlight_hours} hours is too low (min 2)")
        else:
            print(f"Plant {plant_name} is Healthy !\n")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n\n")
    print("Testing good values...")
    check_plant_health('Khyara', 5, 3)
    print()
    print("Testing empty plant name...")
    check_plant_health(None, 5, 3)
    print()
    print("Testing bad water level...")
    check_plant_health("khizowa", 200, 5)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("Maticha", 5, 0)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

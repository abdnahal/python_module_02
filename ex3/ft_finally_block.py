def water_plants(plant_list):
    print("Opening watering system")
    try:
        for i in range(len(plant_list)):
            if not plant_list[i]:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant_list[i]}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n\n")
    print("Testing normal watering...")
    water_plants(['tomato', 'orange', 'avocado'])
    print()
    print("Testing with error...")
    water_plants(['tomato', 'orange', 'avocado', None])


if __name__ == "__main__":
    test_watering_system()
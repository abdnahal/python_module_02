def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n\n")
    print("Testing normal watering...")
    water_plants(['tomato', 'orange', 'avocado'])
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(['tomato', 'orange', 'avocado', None])


if __name__ == "__main__":
    test_watering_system()

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_status(wilting: bool, water_level: int) -> None:
    if wilting and not water_level:
        raise GardenError("The tomato plant is wilting!")
    elif water_level == 0:
        raise WaterError("Not enough water in the tank!")
    elif wilting:
        raise PlantError("The tomato plant is wilting!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_status(True, 5)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_status(False, 0)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_status(True, 5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_status(False, 0)
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")

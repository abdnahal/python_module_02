class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_status(wilting, water_level):
    if wilting and not water_level:
        raise GardenError("General garden failure")
    elif water_level == 0:
        raise WaterError("Not enough water in the tank!")
    elif wilting:
        raise PlantError("The plant is wilting")


if __name__ == "__main__":
    print("=== Abdnahal's custom errors ===")
    print()
    print("Testing WaterError")
    try:
        check_status(False, 0)
    except WaterError as e:
        print(f"Caught a WaterError: {e}\n")
    print("Testing PlantError")
    try:
        check_status(True, 5)
    except PlantError as e:
        print(f"Caught a PlantError: {e}\n")
    print("Testing GardenErrror")
    try:
        check_status(True, 0)
    except GardenError as e:
        print(f"Caught a GardenError: {e}\n")
    print()
    print("All custom error types work correctly!")

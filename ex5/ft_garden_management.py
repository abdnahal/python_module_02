class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self, name, water_level, sunlight, plant_list):
        self.name = name
        self.water = water_level
        self.sunlight = sunlight
        self.plants = plant_list
        
    def check_health(self):
        try:
            for plant in self.plants:
                if not plant:
                    raise PlantError("Plant name cannot be empty!")
                elif self.water > 10:
                    raise GardenError(f"Water level {self.water} is too high (max 10)")
                elif self.water < 1:
                    raise GardenError(f"Water level {self.water} is too low (min 1)")
                elif self.sunlight > 12:
                    raise GardenError(f"{self.sunlight} hours is too high (max 12)")
                elif self.sunlight < 2:
                    raise GardenError(f"{self.sunlight} hours is too low (min 2)")
                else:
                    print(f"Plant {plant} is Healthy!")
        except (PlantError, WaterError, GardenError) as e:
            print(f"Error checking {plant}: {e}")

    def add_plants(self, plant_list):
        print("Adding plants to garden...")
        try:
            for plant in plant_list:
                if not plant:
                    raise PlantError("Plant name cannot be empty!")
                else:
                    print(f"Added {plant} - Success")
        except PlantError as e:
            print(f"Error adding plant: {e}")
        finally:
            print("Finished adding plants")

    def water_plants(self, plant_list):
        print("Opening watering system")
        try:
            for plant in plant_list:
                if not plant:
                    raise WaterError("Plant name cannot be empty!")
                else:
                    print(f"Watering {plant} - Success")
        except WaterError as e:
            print(f"Error Watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management():
    plants = ['khyara', 'khizowa', 'lkhoss', 'denjal']
    alice = GardenManager("alice", 5, 5, plants)
    alice.add_plants(plants)
    alice.add_plants([None])
    print()
    alice.water_plants(plants)
    print()
    alice.check_health()


if __name__ == "__main__":
    test_garden_management()
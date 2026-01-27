class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass


def check_status(wilting):
    if wilting:
        raise PlantError("the plant is wilting")
    

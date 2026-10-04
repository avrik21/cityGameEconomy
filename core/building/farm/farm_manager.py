from core.building.farm.farm import Farm

class FarmManager:
    def __init__(self, city):
        self.city = city

    def upgrade_farm(self, farm_id):
        if not isinstance(farm_id, int):
            return "NOT_INTEGER"
        if farm_id < 0:
            return "INVALID_ID"

        for item in self.city.get_buildings():
            if isinstance(item, Farm) and item.get_id() == farm_id:
                result = item.upgrade_farm()
                if result == "SUCCESS":
                    return "SUCCESS"
                return "MAX_LEVEL"
        return "NO_OBJECT"
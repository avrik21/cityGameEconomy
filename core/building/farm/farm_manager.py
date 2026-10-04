from core.city.city import city

class FarmManager:
    def __init__(self):
        self.city = city

    def upgrade_farm(self, id):
        if not isinstance(id, int):
            return "NOT_INTEGER"
        if id < 0:
            return "NEGATIVE_AMOUNT"

        for item in self.city.get_buildings():
            if item.get_name() == "farm" and item.get_id() == id:
                item.upgrade_farm()
                return "SUCCESS"
        return "NO_OBJECT"

farm_manager = FarmManager()
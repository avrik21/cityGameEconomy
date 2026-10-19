from core.building.farm.farm import Farm

class ProductManager:
    def __init__(self, city):
        self.city = city

    def add_food(self):
        result_food = 0

        if not self.city.get_buildings():
            return "NO_OBJECT"

        for item in self.city.get_buildings():
            if isinstance(item, Farm):
                result_food += item.get_food_per_cycle()

        self.city.add_food(result_food)
        return "SUCCESS"
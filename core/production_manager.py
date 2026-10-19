from core.building.farm.farm import Farm

class ProductManager:
    def __init__(self, city):
        self.city = city

    def add_food(self):
        result_food = 0
        for item in self.city.get_buildings():
            if isinstance(item, Farm):
                result_food += item.food_per_cycle

        if result_food == 0:
            return "NO_OBJECT"

        self.city.add_food(result_food)
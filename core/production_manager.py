from core.building.farm.farm import Farm

class ProductionManager:
    def __init__(self, city):
        self.city = city

    def add_food(self):
        result_food = 0
        signal = 0 
        
        if not self.city.get_buildings():
            return "EMPTY"

        for item in self.city.get_buildings():
            if isinstance(item, Farm):
                result_food += item.get_food_per_cycle()
                signal += 1

        if signal == 0:
            return "NO_FARM"

        if result_food == 0:
            return "NO_FOOD"

        self.city.add_food(result_food)
        return "SUCCESS"
from core.building.building import Building

class Farm(Building):
    def __init__(self, name="farm", construction_cost=1000, maintenance_cost=100):
        super().__init__(name="farm", construction_cost=1000, maintenance_cost=100)
        self.__food_per_cycle = 50
        self.__level = 1

    def upgrade_farm(self):
        if self.__level == 5:
            return "MAX_LEVEL"
        self.__food_per_cycle += 50
        self.__level += 1
        return "SUCCESS"

    def get_food_per_cycle(self):
        return self.__food_per_cycle

    def get_level(self):
        return self.__level
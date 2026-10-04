# from core.building.building import Building
from core.building.building import Building

class Farm(Building):
    def __init__(self, name, construction_cost, maintenance_cost):
        super().__init__(name, construction_cost, maintenance_cost)
        self.food_per_cycle = 50
        self.level = 1

    def upgrade_farm(self):
        if self.level == 5:
            return "MAX_LEVEL"
        self.food_per_cycle += 50
        self.level += 1
        return "SUCCESS"
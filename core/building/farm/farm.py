# from core.building.building import Building
from ..building import Building

class Farm(Building):
    def __init__(self, name, construction_cost, maintenance_cost):
        super().__init__(name, construction_cost, maintenance_cost)
        self.food_per_cycle = 50
        self.level = 1

    def upgrade_farm(self):
        if self.level == 5:
            return "MAXLEVEL"
        self.food_per_cycle += 50
        self.level += 1
        return "SUCCESS"


farm1 = Farm("farm", 1000, 100)
farm2 = Farm("farm", 1000, 100)
farm3 = Farm("farm", 1000, 100)
farm4 = Farm("farm", 1000, 100)

print(farm1.__dict__)
print(farm2.__dict__)
print(farm3.__dict__)
print(farm4.__dict__)
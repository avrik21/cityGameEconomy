from building import Building

class Farm(Building):
    def __init__(self, name, construction_cost, maintenance_cost):
        super().__init__(name, construction_cost, maintenance_cost)
        self.food_per_cycle = 50
        self.lvl = 1

    def upgrade_farm(self):
        self.food_per_cycle += 50
        self.lvl += 1
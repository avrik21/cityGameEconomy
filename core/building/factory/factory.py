from core.building.building import Building

class Factory(Building):
    def __init__(self, name, construction_cost, maintenance_cost):
        super().__init__(name, construction_cost, maintenance_cost)
        self.product_per_cycle = 20
        self.raw_material = 10
        self.level = 1

    def upgrade_factory(self):
        if self.level == 5:
            return "MAX_LEVEL"
        self.product_per_cycle += 20
        self.raw_material += 5
        self.level += 1
        return "SUCCESS"
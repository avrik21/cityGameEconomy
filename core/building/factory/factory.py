from core.building.building import Building

class Factory(Building):
    def __init__(self, name, construction_cost, maintenance_cost):
        super().__init__(name, construction_cost, maintenance_cost)
        self.__product_per_cycle = 20
        self.__raw_material = 10
        self.__level = 1

    def upgrade_factory(self):
        if self.__level == 5:
            return "MAX_LEVEL"
        self.__product_per_cycle += 20
        self.__raw_material += 5
        self.__level += 1
        return "SUCCESS"
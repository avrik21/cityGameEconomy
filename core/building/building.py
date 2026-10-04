class Building:
    def __init__(self, name, construction_cost, maintenance_cost):
        self.name = name
        self.construction_cost = construction_cost
        self.maintenance_cost = maintenance_cost

    def get_name(self):
        return self.name

    def get_construction_cost(self):
        return self.construction_cost

    def get_maintenance_cost(self):
        return self.maintenance_cost
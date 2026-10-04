class Building:
    def __init__(self, name, construction_cost, maintenance_cost):
        self.__name = name
        self.__construction_cost = construction_cost
        self.__maintenance_cost = maintenance_cost

    def get_name(self):
        return self.__name

    def get_construction_cost(self):
        return self.__construction_cost

    def get_maintenance_cost(self):
        return self.__maintenance_cost
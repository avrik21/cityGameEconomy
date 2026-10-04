class Building:    
    __number_id = 1
    def __init__(self, name, construction_cost, maintenance_cost):
        self.__name = name
        self.__construction_cost = construction_cost
        self.__maintenance_cost = maintenance_cost
        self.__id = self.__number_id
        Building.__number_id += 1

    def get_name(self):
        return self.__name

    def get_construction_cost(self):
        return self.__construction_cost

    def get_maintenance_cost(self):
        return self.__maintenance_cost

    def get_id(self):
        return self.__id
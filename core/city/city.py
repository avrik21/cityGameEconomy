class City:
    def __init__(self):
        self.__money = 1000
        self.__citizens = 100
        self.__food = 300
        self.__buildings = []

    def get_money(self):
        return self.__money

    def get_citizens(self):
        return self.__citizens

    def get_food(self):
        return self.__food

    def add_building(self, building):
        self.__buildings.append(building)
        
    def remove_building(self, building):
        self.__buildings.remove(building)

    def get_buildings(self):
        return self.__buildings

    def add_money(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount < 0:
            return "NEGATIVE_AMOUNT"

        self.__money += amount
        return "SUCCESS"

    def spend_money(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount > self.__money:
            return "INSUFFICIENT_MONEY"

        self.__money -= amount
        return "SUCCESS"

    def add_citizens(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount < 0:
            return "NEGATIVE_AMOUNT"

        self.__citizens += amount
        return "SUCCESS"

    def remove_citizens(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount > self.__citizens:
            return "INSUFFICIENT_CITIZENS"
        

        self.__citizens -= amount
        return "SUCCESS"
        
    def add_food(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount < 0:
            return "NEGATIVE_AMOUNT"

        self.__food += amount
        return "SUCCESS"

    def spend_food(self, amount):
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        if amount > self.__food:
            return "INSUFFICIENT_FOOD"

        self.__food -= amount
        return "SUCCESS"

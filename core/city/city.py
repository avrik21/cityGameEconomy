class City:
    def __init__(self):
        self.__money = 1000
        self.__citizens = 100
        self.__food = 300

    def get_money(self):
        return self.__money

    def get_citizens(self):
        return self.__citizens

    def get_food(self):
        return self.__food

    def add_money(self, amount):
        if not amount >= 0:
            return "INSUFFICIENT_MONEY"
        if not isinstance(amount, int):
            return "NOT_INTEGER"

        self.__money += amount
        return "SUCCESS"

    def spend_money(self, amount):
        if not amount > self.__money:
            return "INSUFFICIENT_MONEY"
        if not isinstance(amount, int):
            return "NOT_INTEGER"

        self.__money -= amount
        return "SUCCESS"

    def add_citizens(self, amount):
        if not amount >= 0:
            return "INSUFFICIENT_CITIZENS"
        if not isinstance(amount, int):
            return "NOT_INTEGER"

        self.__citizens += amount
        return "SUCCESS"

    def remove_citizens(self, amount):
        if not amount > self.__citizens:
            return "INSUFFICIENT_CITIZENS"
        if not isinstance(amount, int):
            return "NOT_INTEGER"
        

        self.__citizens -= amount
        return "SUCCESS"
        
    def add_food(self, amount):
        if not amount >= 0:
            return "INSUFFICIENT_FOOD"
        if not isinstance(amount, int):
            return "NOT_INTEGER"

        self.__food += amount
        return "SUCCESS"

    def spend_food(self, amount):
        if not amount > self.__food:
            return "INSUFFICIENT_FOOD"
        if not isinstance(amount, int):
            return "NOT_INTEGER"

        self.__food -= amount
        return "SUCCESS"
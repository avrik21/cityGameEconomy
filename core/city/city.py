class City:
    def __init__(self):
        self.__money = 1000
        self.__citizens = 100
        self.__food = 300

    def get_money(self):
        return self.__money

    def get_citizen(self):
        return self.__citizens

    def get_food(self):
        return self.__food

    def add_money(self, amount):
        if not amount >= 0 and not isinstance(amount, int):
            return False

        self.__money += amount

    def spend_money(self, amount):
        if not amount > self.__money and not isinstance(amount, int):
            return False

        self.__money -= amount
        
    def add_citizen(self, amount):
        if not amount >= 0 and not isinstance(amount, int):
            return False

        self.__citizens += amount

    def remove_citizen(self, amount):
        if not amount > self.__citizens and not isinstance(amount, int):
            return False

        self.__citizens -= amount
        
    def add_food(self, amount):
        if not amount > 0 and not isinstance(amount, int):
            return False

        self.__food += amount

    def spend_food(self, amount):
        if not amount > self.__food and not isinstance(amount, int):
            return False

        self.__food -= amount
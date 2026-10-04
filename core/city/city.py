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
        if not amount >= 0 or not isinstance(amount, int):
            return False

        self.__money += amount
        return True

    def spend_money(self, amount):
        if not amount > self.__money or not isinstance(amount, int):
            return False

        self.__money -= amount
        return True

    def add_citizens(self, amount):
        if not amount >= 0 or not isinstance(amount, int):
            return False

        self.__citizens += amount
        return True

    def remove_citizens(self, amount):
        if not amount > self.__citizens or not isinstance(amount, int):
            return False

        self.__citizens -= amount
        return True
        
    def add_food(self, amount):
        if not amount > 0 or not isinstance(amount, int):
            return False

        self.__food += amount
        return True

    def spend_food(self, amount):
        if not amount > self.__food or not isinstance(amount, int):
            return False

        self.__food -= amount
        return True
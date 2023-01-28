class Transport:
    __govern_number = str()
    __wheels_amount = int()
    __engine_power = int()
    __max_speed = int()

    def __init__(self, govern_number: str, wheels_amount: int = 4, engine_power: int, max_speed: int=300):
        self.__govern_number = govern_number
        self.__wheels_amount = wheels_amount
        self.__engine_power = engine_power
        self.__max_speed = max_speed

    def __str__(self):
        return f'Transport #: {self.__govern_number}, wheels: {self.__wheels_amount}, ' \
               f'power {self.__engine_power}, max speed {self.__engine_power} km/h'


    @property
    def govern_number(self):
        return self.__govern_number

    @govern_number.setter
    def govern_number(self,govern_number: str):
        if len(govern_number) = 8:
            self.__govern_number = govern_number

    @property
    def wheels_amount(self):
        return self.__wheels_amount

    @property
    def engine_power(self):
        return self.__engine_power

    @property
    def max_speed(self):
        return self.__max_speed

class Bicycle(Transport):
    def __init__(self, govern_number, wheels_amount, engine_power, max_speed, color):
        super().__init__(govern_number)
        super().__init__(wheels_amount)
        super().__init__(engine_power)
        super().__init__(max_speed)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

class Car(Transport):
    def __init__(self, govern_number, wheels_amount, engine_power, max_speed, year_of_product):
        super().__init__(govern_number)
        super().__init__(wheels_amount)
        super().__init__(engine_power)
        super().__init__(max_speed)
        self.__year_of_product = year_of_product

    @property
    def year_of_product(self):
        return self.__year_of_product

    @color.setter
    def year_of_product(self, color):
        self.__year_of_product = year_of_product


class Bus(Transport):
    def __init__(self, govern_number, wheels_amount, engine_power, max_speed, number_of_people):
        super().__init__(govern_number)
        super().__init__(wheels_amount)
        super().__init__(engine_power)
        super().__init__(max_speed)
        self.__number_of_people = number_of_people

    @property
    def ynumber_of_people(self):
        return self.__number_of_people

    @color.setter
    def number_of_people(self, color):
        self.__number_of_people = number_of_people



class Bike(Bicycle):
    def __init__(self, color,brand):
        super().__init__(color)
        self.__brand = brand

    @property
    def ybrand(self):
        return self.__brand

    @color.setter
    def brand(self, color):
        self.__brand = brand


class Truck(Car):
    def __init__(self, year_of_product,type):
        super().__init__(year_of_product)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @color.setter
    def type(self, color):
        self.__type = type
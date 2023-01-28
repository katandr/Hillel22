class Animal:
    __name = str()
    __weight = int()
    __speed = int()

    def __init__(self, name: str, weight: int, speed: int):
        self.__name = name
        self.__weight = weight
        self.__speed = speed


    def __str__(self):
        return f'Name #: {self.__name}, weight: {self.__weight}, ' \
               f'speed {self.__speed}, km/h'


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name: str):
        self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: iunt):
        self.__weight = weight

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def weight(self, speed: int):
        self.__speed = speed

    def say(self,say: str):
        return f'this animal is saying {say}'

class Birds(Animal):
    def __init__(self, name, weight, speed, height):
        super().__init__(name)
        super().__init__(weight)
        super().__init__(speed)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Reptiles(Animal):
    def __init__(self, name, weight, speed,color):
        super().__init__(name)
        super().__init__(weight)
        super().__init__(speed)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @height.setter
    def color(self, color):
        self.__color = color


class Mammals(Animal):
    def __init__(self, name, weight, speed,years_of_life):
        super().__init__(name)
        super().__init__(weight)
        super().__init__(speed)
        self.__years_of_life = years_of_life

    @property
    def years_of_life(self):
        return self.__years_of_life

    @height.setter
    def years_of_life(self, years_of_life):
        self.__years_of_life = years_of_life


class Seagull(Birds):
    def __init__(self, height, food):
        super().__init__(height)
        self.__food = food

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

class Pigeon(Birds):
    def __init__(self, height, color):
        super().__init__(height)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Iguana(Reptiles):
    def __init__(self,color,temperature):
        super().__init__(color)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature


class Salamander(Reptiles):
    def __init__(self, color, area_of_living):
        super().__init__(color)
        self.__area_of_livinge = area_of_living

    @property
    def area_of_living(self):
        return self.__area_of_living

    @area_of_living.setter
    def area_of_living(self, area_of_living):
        self.__area_of_living = area_of_living


class Zebra(Mammals):
    def __init__(self, years_of_life, live_in_zoo):
        super().__init__(years_of_life)
        self.__live_in_zoo = live_in_zoo

    @property
    def live_in_zoo(self):
        return self.__live_in_zoo

    @live_in_zoo.setter
    def alive_in_zoo(self, live_in_zoo):
        self.__live_in_zoo = live_in_zoo

class Bear(Mammals):
    def __init__(self, years_of_life, sleep_in_winter):
        super().__init__(years_of_life)
        self.__sleep_in_winter = sleep_in_winter

    @property
    def sleep_in_winter(self):
        return self.__sleep_in_winter

    @sleep_in_winter.setter
    def sleep_in_winter(self, sleep_in_winter):
        self.__sleep_in_winter = sleep_in_winter
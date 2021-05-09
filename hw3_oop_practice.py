from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def provide_info_person(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, availability_of_money, own_house=[], job=None, salary=0):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.own_house = own_house
        self.job = job
        self.salary = salary

    def provide_info_person(self):
        print(f'My name is {self.name}. I am {self.age} years old.')
        print(f'Currently I have {self.availability_of_money} dollars.')
        if {self.job} is not None:
            print(f'I work as {self.job} and my salary is {self.salary}.')

    def make_money(self):
        print('---Making money---')
        print(f'Before I got the salary my availability of money was: {self.availability_of_money}')
        self.availability_of_money += self.salary
        print(f'Now after the salary I have {self.availability_of_money} dollars.')

    def buy_house(self, house, realtor):
        if self.availability_of_money < house.cost:
            print('Unfortunately you do not have enought money to buy the house')
        else:
            self.availability_of_money -= house.cost
            self.own_house.append(house)
            print('I have my new own house.')


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_purchase_discount(self, purchase_discount=0):
        self.cost = (1 - purchase_discount / 100) * self.cost
    # print(f'Now the house costs {self.cost} dollars.')


class RealtorType(type):
    _instances = {}

    def call(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def provide_info_about_houses(self):
        raise NotImplementedError

    def give_discount(self):
        raise NotImplementedError

    def Steal_your_money(self):
        raise NotImplementedError


class Realtor(metaclass=RealtorType):
    def __init__(self, name, houses=[], discount=0):
        self.name = name
        self._houses = self.create_house_list(houses)
        self.discount = discount

    def create_house_list(self, houses):
        house_list = []
        for house in houses:
            house_list.append(house)
        return house_list

    def provide_info_about_houses(self):
        print(f'I am a realtor and currently I have such houses to sell:')
        for house in self._houses:
            print(f'- House with area {house.area} m2, that costs {house.cost} dollars.')

    def give_discount(self, house):
        if house in self._houses:
            house.apply_purchase_discount(self.discount)
            print(f'The price after the discount of {self.discount} % equal to {house.cost} ')
        else:
            print('This house can not be sold my this realtor.')

    def Steal_your_money(self):
        pass


person_instance = Person('John', 30, 100000, salary=100)
house_instance_1 = House(40, 100000)
house_instance_2 = House(55, 120000)
realtor_instance_1 = Realtor('Mark', [house_instance_1, house_instance_2], 15)

person_instance.provide_info_person()
person_instance.make_money()
person_instance.buy_house(house_instance_1, realtor_instance_1)
person_instance.provide_info_person()
# house_instance_1.apply_purchase_discount(10)
realtor_instance_1.provide_info_about_houses()
realtor_instance_1.give_discount(house_instance_1)

from abc import ABC, abstractmethod
import random


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
        print(f'My name is {self.name}. I am {self.age} years old.' + '\n'
        f'Currently I have {self.availability_of_money} dollars.' + '\n'
              f'I work as {self.job} and my salary is {self.salary}.')

    def make_money(self):
        print(f'Before I got the salary my budget was: {self.availability_of_money}')
        self.availability_of_money += self.salary
        print(f'Now after the salary I have {self.availability_of_money} dollars.')

    def buy_house(self, house, realtor):
        if self.availability_of_money < house.cost:
            print(f'Unfortunately you do not have enough money to buy this house with area of {house.area} m2.' + '\n'
            f'You can try to review other houses.')
        else:
            self.availability_of_money -= house.cost
            self.own_house.append(house)
            print('I bought a house and now I have my new own home.')


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def apply_purchase_discount(self, purchase_discount=0):
        self.cost = (1 - purchase_discount / 100) * self.cost


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

    def steal_money(self):
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
        print(f'Hi, I am a realtor and currently I have such houses to sell:')
        for house in self._houses:
            print(f'- House with area {house.area} m2, that costs {house.cost} dollars.')

    def give_discount(self, house):
        if house in self._houses:
            house.apply_purchase_discount(self.discount)
            print(
                f'The price of house with area of {house.area} m2 after the discount of {self.discount} % equal to {house.cost} .')
        else:
            print('This house can not be sold by this realtor.')

    def steal_money(self, person):
        percentage_chance = 10
        if random.randint(1, 15) < percentage_chance:
            stolen_money = random.randint(100, 1000)
            if person.availability_of_money > stolen_money:
                person.availability_of_money -= stolen_money
                print(
                    f'The realtor stole {stolen_money} dollars and now person has only {person.availability_of_money} dollars.')
            else:
                person.availability_of_money = 0
                print(f'Unfortunately everything was stolen, and person does not have money anymore.')
        else:
            print(f'Nothing was stolen.')


person_instance = Person('John', 30, 100000, job='teacher', salary=1500)
house_instance_1 = House(40, 100000)
house_instance_2 = House(55, 120000)
realtor_instance_1 = Realtor('Mark', [house_instance_1, house_instance_2], 15)

person_instance.provide_info_person()
person_instance.make_money()
realtor_instance_1.provide_info_about_houses()
realtor_instance_1.give_discount(house_instance_2)
person_instance.buy_house(house_instance_2, realtor_instance_1)
realtor_instance_1.give_discount(house_instance_1)
person_instance.buy_house(house_instance_1, realtor_instance_1)
realtor_instance_1.steal_money(person_instance)

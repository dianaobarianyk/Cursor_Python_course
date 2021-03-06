# 1.Create a class hierarchy of animals with at least 5 animals that have additional methods each, create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class


class Animals:
    def __init__(self, animal_name):
        self.animal_name = animal_name


def eat(self):
    print(f'I am {self.animal_name}  and I eat')


def sleep(self):
    print(f'I am {self.animal_name}  and I sleep')


class Dog(Animals):
    def bark(self):
        print(f'I am {self.animal_name} and I bark')


class Bird(Animals):
    def sing(self):
        print(f'I am {self.animal_name} and I sing')


class Horse(Animals):
    def ride(self):
        print(f'I am {self.animal_name} and I ride')


class Fish(Animals):
    def swim(self):
        print(f'I am {self.animal_name} and I swim')


class Chameleon(Animals):
    def change_color(self):
        print(f'I am {self.animal_name} and I change the color')


dog = Dog('Sirko')
bird = Bird('Kesha')
horse = Horse('Vinni')
fish = Fish('Nemo')
chameleon = Chameleon('Rikky')

dog.bark()
bird.sing()
horse.ride()
fish.swim()
chameleon.change_color()

print(f'Checking if objects are instances of Animals class')
print('---------------------------------------------------')
print(f'The dog is an animal : {isinstance(dog, Animals)}')
print(f'The bird is an animal : {isinstance(bird, Animals)}')
print(f'The horse is an animal : {isinstance(horse, Animals)}')
print(f'The fish is an animal : {isinstance(fish, Animals)}')
print(f'The chameleon is an animal : {isinstance(chameleon, Animals)}')


# 1.a.Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur
# class and call the common method of these classes and unique.


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'I am {self.name} and I am eating')

    def sleep(self):
        print(f'I am {self.name} and I am sleeping')

    def study(self):
        print(f'I am {self.name} and I am studying')

    def work(self):
        print(f'I am {self.name} and I am working')


class Centaur(Human, Animals):
    def relax(self):
        print(f'I am {self.name} and I am relaxing')


centaur = Centaur('Dan')
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.relax()


# 2. Create two classes: Person, CellPhone, one for composition, another one for aggregation.
# a.


class Person:
    def __init__(self):
        left_arm = Arm(25, 'white', 'left')
        right_arm = Arm(25, 'white', 'right')
        self.arms = (left_arm, right_arm)


class Arm:
    def __init__(self, length, color, type):
        self.length = length
        self.color = color
        self.type = type


young_person = Person()
print('-----------------------------')
for arm in young_person.arms:
    print(f'I am person and I have {arm.type} {arm.color} arm with length of {arm.length} sm')


# b.

class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self):
        pass


screen = Screen()
iphone = CellPhone(screen)

# 3. class Profile:
"""

Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex

Override a printable string representation of Profile class and return: list of the params mentioned above
"""


class Profile:
    def __init__(self, name, last_name, phone, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.representation = [self.name, self.last_name, self.phone, self.address, self.email, self.birthday, self.age,
                               self.sex]

    def __str__(self):
        return f'{self.representation}'


New_Profile = Profile('David', 'Cursor', '+380000001111', 'Lviv', 'dcursor@gmail.com', '21.10.1991', 30, 'male')
print(New_Profile.__str__())

# 4. * Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics and create
# an HPLaptop class by using your interface.


from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keybord(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, model, year, ssd, screen_size, keybord_type, touchpad_type, webcam_type, port, dynamic_type):
        self.model = model
        self.year = year
        self.ssd = ssd
        self.screen_size = screen_size
        self.keybord_type = keybord_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.port = port
        self.dynamic_type = dynamic_type

    def screen(self):
        print(f'HPLaptop screen size of model {self.model} is {self.screen_size}.')

    def keybord(self):
        print(f'HPLaptop keybord type is {self.keybord_type}.')

    def touchpad(self):
        print(f'HPLaptop touchpad type is {self.touchpad_type}.')

    def webcam(self):
        print(f'HPLaptop webcam is {self.webcam_type}.')

    def ports(self):
        print(f'HPLaptop port is {self.port}.')

    def dynamics(self):
        print(f'HPLaptop dynamics is {self.dynamic_type}.')


my_hplaptop = HPLaptop('HP Pavilion 15-eg0001ua Natural Silver', '2020', '256 GB', 15.6, 'HP Keybord', 'HP TouchPad 4G',
                       'Logitech HD Webcam C920', '2 ?? 3.2 Gen 1 USB', 'GD6000')

my_hplaptop.screen()
my_hplaptop.keybord()
my_hplaptop.touchpad()
my_hplaptop.webcam()
my_hplaptop.ports()
my_hplaptop.dynamics()

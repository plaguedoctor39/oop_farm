from abc import *


class Animal(metaclass=ABCMeta):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __del__(self):
        print(f'Объект класса {self.__class__.__name__} с именем {self.name} был удален')

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def do_voice(self):
        pass


class Goose(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Goose voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name} и '
            f'полем weight -> {self.weight}')

    def collect_eggs(self):
        print(f'Яйца у объекта класса {self.__class__.__name__} с именем {self.name} собраны!')


class Cow(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Moo voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name} '
            f'и полем weight -> {self.weight}')

    def get_milk(self):
        print(f'Вы собрали молоко у объекта класса {self.__class__.__name__} с именем {self.name}')


class Goat(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Goat voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name} '
            f'и полем weight -> {self.weight}')

    def get_milk(self):
        print(f'Вы собрали молоко у объекта класса {self.__class__.__name__} с именем {self.name}')


class Duck(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Duck voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name} '
            f'и полем weight -> {self.weight}')

    def collect_eggs(self):
        print(f'Яйца у объекта класса {self.__class__.__name__} с именем {self.name} собраны!')


class Chicken(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Chicken voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name}'
            f' и полем weight -> {self.weight}')

    def collect_eggs(self):
        print(f'Яйца у объекта класса {self.__class__.__name__} с именем {self.name} собраны!')


class Sheep(Animal):
    def do_voice(self):
        print(f'{self.name} do {self.voice}')

    def feed(self):
        print(f'Вы покормили животное класса {self.__class__.__name__} с именем {self.name}')

    def __init__(self, name, weight):
        Animal.__init__(self, name, weight)
        self.voice = 'Sheep voice'
        print(
            f'Создан объект класса {self.__class__.__name__} с полем name -> {self.name} '
            f'и полем weight -> {self.weight}')

    def get_wool(self):
        print(f'Шерсть у объекта класса {self.__class__.__name__} с именем {self.name} была собрана!')


def feed_all():
    for animals in farm.values():
        for animal in animals:
            animal.feed()


def do_activity():
    for animals_type in farm:
        if animals_type == 'Goose' or animals_type == 'Chicken' or animals_type == 'Duck':
            for animal in farm[animals_type]:
                animal.collect_eggs()
        elif animals_type == 'Cow' or animals_type == 'Goat':
            for animal in farm[animals_type]:
                animal.get_milk()
        elif animals_type == 'Sheep':
            for animal in farm[animals_type]:
                animal.get_wool()


def voice_check():
    for animals in farm.values():
        for animal in animals:
            animal.do_voice()


def total_weight():
    weight_sum = 0
    for animals in farm.values():
        for animal in animals:
            weight_sum += animal.weight
    return weight_sum


def the_heaviest():
    max_weight = 0
    for animals in farm.values():
        for animal in animals:
            if animal.weight > max_weight:
                max_weight = animal.weight
                the_heaviest_animal = animal
    return the_heaviest_animal


def show_all_names(filter='all'):
    if filter == 'all':
        for animals in farm.values():
            for animal in animals:
                print(animal.name)
    elif filter == 'milk':
        for animals in farm:
            if animals == 'Cow' or animals == 'Goat':
                for animal in farm[animals]:
                    print(animal.name)
    elif filter == 'eggs':
        for animals in farm:
            if animals == 'Chicken' or animals == 'Duck' or animals == 'Goose':
                for animal in farm[animals]:
                    print(animal.name)
    elif filter == 'wool':
        for animals in farm:
            if animals == 'Sheep':
                for animal in farm[animals]:
                    print(animal.name)


def check_name(name):
    for animals in farm.values():
        for animal in animals:
            if animal.name.lower() == name:
                return 1
    return 0


def get_obj_by_name(name):
    for animals in farm.values():
        for animal in animals:
            if animal.name.lower() == name:
                return animal


def show_types():
    for type in farm:
        print(type)


def check_type(type):
    for types in farm:
        if types.lower() == type:
            return 1
    return 0


def animal_add(type):  # TODO: добавить возможность добавлять новых животных с помощью функции
    #name = input('Введите имя - ')
    #weight = input('Введите вес - ')
    print("Животных пока добавлять нельзя")


grey_goose = Goose('Серый', 10)
white_goose = Goose('Белый', 7)
Cow1 = Cow('Манька', 30)
Goat1 = Goat('Рога', 12)
Goat2 = Goat('Копыта', 14)
Duck1 = Duck('Кряква', 6)
Chicken1 = Chicken('Ко-ко', 4)
Chicken2 = Chicken('Кукареку', 3)
Sheep1 = Sheep('Барашек', 9)
Sheep2 = Sheep('Кудрявый', 12)

farm = {
    'Goose': [grey_goose, white_goose],
    'Cow': [Cow1],
    'Goat': [Goat1, Goat2],
    'Duck': [Duck1],
    'Chicken': [Chicken1, Chicken2],
    'Sheep': [Sheep1, Sheep2]
}


def runner():
    while True:
        cmd = input('Введите команду - ').lower()
        if cmd == 'fa' or cmd == 'feed all':
            feed_all()
        elif cmd == 'f' or cmd == 'feed':
            print('Выберите кого вы хотите покормить: ')
            show_all_names()
            animal_to_feed = input('Введите имя - ').lower()
            if check_name(animal_to_feed) == 1:
                get_obj_by_name(animal_to_feed).feed()
            else:
                print(f'Животного с именем {animal_to_feed} нету на ферме')
        elif cmd == 'doaa' or cmd == 'do all activities':
            do_activity()
        elif cmd == 'v' or cmd == 'voice':
            print('Выберите кого вы хотите послушать: ')
            show_all_names()
            animal_to_speak = input('Введите имя - ').lower()
            if check_name(animal_to_speak) == 1:
                get_obj_by_name(animal_to_speak).do_voice()
            else:
                print(f'Животного с именем {animal_to_speak} нету на ферме')
        elif cmd == 'vc' or cmd == 'voice check':
            voice_check()
        elif cmd == 'tw' or cmd == 'total weight':
            print(f'Общий вес всех животных на ферме {total_weight()}кг')
        elif cmd == 'w' or cmd == 'weight':
            print('Выберите имя животного, вес которого вы хотите узнать: ')
            show_all_names()
            animal_weight_check = input('Введите имя - ').lower()
            if check_name(animal_weight_check) == 1:
                print(f'Животное класса {get_obj_by_name(animal_weight_check).__class__.__name__} с именем '
                      f'{get_obj_by_name(animal_weight_check).name} весит'
                      f' {get_obj_by_name(animal_weight_check).weight}кг')
            else:
                print(f'Животного с именем {animal_weight_check} нету на ферме')
        elif cmd == 'th' or cmd == 'the heaviest':
            print(f'Самое тяжелое животное на ферме это {the_heaviest().name} с весом {the_heaviest().weight}кг')
        elif cmd == 'a' or cmd == 'add':
            show_types()
            animal_type = input('Введите тип животног, которое вы хотите добавить на ферму - ')
            if check_type(animal_type) == 1:
                animal_add(animal_type)
            else:
                print(f'Животных типа {animal_type} нету на ферме')
        elif cmd == 'gm' or cmd == 'get milk':
            print('Выберите животное чье молоко вы хотите получить: ')
            show_all_names('milk')
            animal_get_milk = input('Введите имя - ').lower()
            if check_name(animal_get_milk) == 1:
                get_obj_by_name(animal_get_milk).get_milk()
            else:
                print(f'Животного с именем {animal_get_milk} нету на ферме')
        elif cmd == 'ce' or cmd == 'collect eggs':
            print('Выберите животное чьи яйца вы хотите получить: ')
            show_all_names('eggs')
            animal_collect_eggs = input('Введите имя - ').lower()
            if check_name(animal_collect_eggs) == 1:
                get_obj_by_name(animal_collect_eggs).collect_eggs()
            else:
                print(f'Животного с именем {animal_collect_eggs} нету на ферме')
        elif cmd == 'gw' or cmd == 'get wool':
            print('Выберите животное чью шерсть вы хотите получить: ')
            show_all_names('wool')
            animal_get_wool = input('Введите имя - ').lower()
            if check_name(animal_get_wool) == 1:
                get_obj_by_name(animal_get_wool).get_wool()
            else:
                print(f'Животного с именем {animal_get_wool} нету на ферме')
        elif cmd == 'e' or cmd == 'end':
            print('Программа завершена')
            break
        else:
            print(f'Команды {cmd} нету в списке доступных команд')


runner()

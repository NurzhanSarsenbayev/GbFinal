from AnimalRegistry_python.HumanFriends import *


class ModelRegistry:
    def __init__(self):
        self.__animals = []

    @property
    def animals(self):
        return self.__animals
    def add_animal(self, animal_type, animal_name, date_of_birth, commands_list):
        if animal_type == 1:
            self.__animals.append(Dog(animal_name, date_of_birth, commands_list))
        if animal_type == 2:
            self.__animals.append(Cat(animal_name, date_of_birth, commands_list))
        if animal_type == 3:
            self.__animals.append(Hamster(animal_name, date_of_birth, commands_list))
        if animal_type == 4:
            self.__animals.append(Horse(animal_name, date_of_birth, commands_list))
        if animal_type == 5:
            self.__animals.append(Camel(animal_name, date_of_birth, commands_list))
        if animal_type == 6:
            self.__animals.append(Donkey(animal_name, date_of_birth, commands_list))

    def add_commands(self, animal_id, commands_list):
        for animal in self.__animals:
            if animal_id == animal.id:
                animal.list_of_commands.extend(commands_list)

    def sort_by_birth(self):
        return self.__animals.sort(key=lambda animal: animal.date_of_birth)

    def sort_by_id(self):
        return self.__animals.sort(key=lambda animal: animal.id)

    def show_commands(self):
        animal_id = int(input("What animal? Type their ID "))
        for animal in self.__animals:
            if animal_id == animal.id:
                print(animal.list_of_commands)

    def show_count_pet_package(self, animal_type):
        if animal_type == 1:
            print("Count is {}".format(Pet.count))
        elif animal_type == 2:
            print("Count is {}".format(PackageAnimal.count))
        else:
            print("No such type.")

    def delete_animal(self, animal_id):
        for animal in self.__animals:
            if animal_id == animal.id:
                self.__animals.remove(animal)
                if isinstance(animal, Dog):
                    Dog.count -= 1
                    Pet.count -= 1
                    print('Animal deleted')
                elif isinstance(animal, Cat):
                    Cat.count -= 1
                    Pet.count -= 1
                    print('Animal deleted')
                elif isinstance(animal, Hamster):
                    Hamster.count -= 1
                    Pet.count -= 1
                    print('Animal deleted')
                elif isinstance(animal, Horse):
                    Horse.count -= 1
                    PackageAnimal.count -= 1
                    print('Animal deleted')
                elif isinstance(animal, Camel):
                    Camel.count -= 1
                    PackageAnimal.count -= 1
                    print('Animal deleted')
                elif isinstance(animal, Donkey):
                    Donkey.count -= 1
                    PackageAnimal.count -= 1
                    print('Animal deleted')


    def delete_commands(self, animal_id):

        for animal in self.__animals:
            if animal_id == animal.id:
                print("Commands: {}".format(animal.list_of_commands))
                index = int(input('Type index of command to delete. '))
                animal.list_of_commands.pop(index)

    def show_count_by_type(self, animal_type):
        if animal_type == 1:
            print("Count is {}".format(Dog.count))
        if animal_type == 2:
            print("Count is {}".format(Cat.count))
        if animal_type == 3:
            print("Count is {}".format(Hamster.count))
        if animal_type == 4:
            print("Count is {}".format(Horse.count))
        if animal_type == 5:
            print("Count is {}".format(Camel.count))
        if animal_type == 6:
            print("Count is {}".format(Donkey.count))


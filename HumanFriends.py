class Animal:
    next_id = 1

    def __init__(self, name, animal_type, date_of_birth, list_of_commands=[]):
        self.name = name
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.list_of_commands = list_of_commands
        self.id = Animal.next_id
        Animal.next_id += 1

    def __repr__(self):
        return ("ID {} {} : {}, {}").format(self.id, self.name, self.animal_type, self.date_of_birth)

    #    def __repr__(self):
    #       return ("{} is a {}, it was born in {} and it can do these commands: {}. Overall there are {} members of this "
    #              "class").format(self.name, self.animal_type,
    #                             self.date_of_birth,
    #                            self.list_of_commands, self.count)

    #def commands_list(self):
    #    return print("{} is a {} and can do these commands : {}".format(self.name, self.animal_type, self.list_of_commands))

    # Commented out is a code that I initially planned, but decided to ditch for functionality


class Pet(Animal):
    count = 0


class PackageAnimal(Animal):
    count = 0


class Cat(Pet):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Cat", date_of_birth, list_of_commands)
        Cat.count += 1
        Pet.count += 1


class Dog(Pet):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Dog", date_of_birth, list_of_commands)
        Dog.count += 1
        Pet.count += 1


class Hamster(Pet):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Hamster", date_of_birth, list_of_commands)
        Hamster.count += 1
        Pet.count += 1


class Horse(PackageAnimal):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Horse", date_of_birth, list_of_commands)
        Horse.count += 1
        PackageAnimal.count += 1


class Donkey(PackageAnimal):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Donkey", date_of_birth, list_of_commands)
        Donkey.count += 1
        PackageAnimal.count += 1


class Camel(PackageAnimal):
    count = 0

    def __init__(self, name, date_of_birth, list_of_commands):
        super().__init__(name, "Camel", date_of_birth, list_of_commands)
        Camel.count += 1
        PackageAnimal.count += 1


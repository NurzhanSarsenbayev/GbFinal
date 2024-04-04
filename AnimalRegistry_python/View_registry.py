
from datetime import date

# View
class ViewRegistry:

    @staticmethod
    def input_string(prompt):
        return input(prompt)
    @staticmethod
    def input_animal():
        animal_name = input("What's the name of the animal? ")
#        animal_type = input("What's the type of the animal? We have Dog, Cat, Hamster, Horse, Camel and Donkey ").capitalize()
#        if animal_type not in ['Dog', 'Cat', 'Hamster', 'Horse', 'Camel', 'Donkey']:
#            print("We don't cover this type of animal. It was defaulted to Dog ")
#            animal_type = 'Dog'
        # Commented out is a code that I initially planned, but decided to ditch for functionality
        while True:
            try:
                print("Please write valid integer")
                animal_type_temp = int(input("What's the type of the animal: 1) Dog, 2) Cat, 3) Hamster, 4) Horse, "
                                             "5) Camel, 6) Donkey "))
                if 1 <= animal_type_temp <= 6:
                    animal_type = animal_type_temp
                    break
                else:
                    print("Invalid input. Please enter valid integers from 1 to 6")
            except ValueError:
                print("Invalid input. Please enter valid integers.")

        while True:
            try:
                year = int(input('What is its birthday? Type year: '))
                month = int(input('Type month: '))
                day = int(input('Type day: '))
                date(year, month, day)
                break
            except ValueError:
                print("Invalid input. Please enter valid integers for year, month, and day.")
            except ValueError as e:
                print("Invalid date:", e)
        print("Date entered successfully:", year, month, day)
        date_of_birth = date(year, month, day)
        commands_list = []
        while True:
            commands_input = input(
                'What commands does the animal know? (or type "stop" to exit): ')
            if commands_input.lower() == "stop":
                print("Exiting...")
                break
            new_commands = commands_input.split(',')
            commands_list.extend(new_commands)
            print("Updated list of commands:", commands_list)
        print('Animal successfully created')
        return animal_type, animal_name, date_of_birth, commands_list

    @staticmethod
    def input_additional_commands():
        animal_id = int(input("What animal should learn new commands? Type its ID "))
        commands_list = []
        while True:
            commands_input = input(
                'What commands would you like to add? (or type "stop" to exit): ')
            if commands_input.lower() == "stop":
                print("Exiting...")
                break
            new_commands = commands_input.split(',')
            commands_list.extend(new_commands)
            print("Updated list of commands:", commands_list)
        return animal_id, commands_list

    @staticmethod
    def display_animals(animals):
        print(animals)

    @staticmethod
    def input_type_pet_package():
        while True:
            try:
                animal_type = int(input("What count: Pet (1) or PackageAnimal (2)? Please type integers "))
                if 1 <= animal_type <= 2:
                    return animal_type
                else:
                    print("Invalid input. Please enter valid integers (1 or 2)")
            except ValueError:
                print("Invalid input. Please enter valid integers.")


    @staticmethod
    def input_animal_by_id():
        while True:
            try:
                animal_id = int(input("What is the animals ID? "))
                return animal_id
            except ValueError:
                print("Invalid input. Please enter valid integers.")

    @staticmethod
    def input_type():
        while True:
            try:
                animal_type = int(input("What count: 1) Dog, 2) Cat, 3) Hamster, 4) Horse, 5) Camel, 6) Donkey "))
                if 1 <= animal_type <= 6:
                    return animal_type
                else:
                    print("Invalid input. Please enter valid integers from 1 to 6")
            except ValueError:
                print("Invalid input. Please enter valid integers.")


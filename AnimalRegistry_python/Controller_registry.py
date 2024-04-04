from Model_registry import *
from View_registry import *


# Controller
class Controller:
    def __init__(self):
        self.model = ModelRegistry()
        self.view = ViewRegistry()

    def add_animal(self):
        animal_type, animal_name, date_of_birth, commands = self.view.input_animal()
        self.model.add_animal(animal_type, animal_name, date_of_birth, commands)

    def add_commands(self):
        animal_id, commands_list = self.view.input_additional_commands()
        self.model.add_commands(animal_id, commands_list)

    def sort_animals_by_birth(self):
        self.model.sort_by_birth()

    def sort_animals_by_id(self):
        self.model.sort_by_id()

    def show_commands(self):
        self.model.show_commands()

    def display_animals(self):
        self.view.display_animals(self.model.animals)

    def show_count_pet_package(self):
        self.model.show_count_pet_package(self.view.input_type_pet_package())

    def delete_animal(self):
        self.model.delete_animal(self.view.input_animal_by_id())

    def delete_command(self):
        self.model.delete_commands(self.view.input_animal_by_id())

    def show_count(self):
        self.model.show_count_by_type(self.view.input_type())

    def run(self):
        while True:
            print("\nCommands:")
            print("1. Add animal")
            print("2. Show animals")
            print("3. Show commands")
            print("4. Add command")
            print("5. Delete command")
            print("6. Show count (Pets or Package)")
            print("7. Show count by type")
            print("8. Show by birthday")
            print("9. Delete animal")
            print("10. Exit")



            choice = self.view.input_string("Enter the number of your choice: ")

            if choice == "1":
                self.add_animal()
            elif choice == "2":
                self.sort_animals_by_id()
                self.display_animals()
            elif choice == "3":
                self.display_animals()
                self.show_commands()
            elif choice == "4":
                self.display_animals()
                self.add_commands()
            elif choice == "5":
                self.display_animals()
                self.delete_command()
            elif choice == '6':
                self.show_count_pet_package()
            elif choice == "7":
                self.show_count()
            elif choice == '8':
                self.sort_animals_by_birth()
                self.display_animals()
            elif choice == '9':
                self.display_animals()
                self.delete_animal()
            elif choice == "10":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 10.")


if __name__ == "__main__":
    controller = Controller()
    controller.run()

import os, json

class Character:
    def __init__(self, name, race, strength, dexterity, constitution):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

def create_character():
    print("Let's create a new D&D character!")
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    strength = int(input("Enter character strength: "))
    dexterity = int(input("Enter character dexterity: "))
    constitution = int(input("Enter character constitution: "))
    return Character(name, race, strength, dexterity, constitution)

def save_to_json(character, filename):
    with open(filename, 'w') as file:
        json.dump(vars(character), file, indent=4)

def check_existing_file(filename):
    return os.path.isfile(filename)

# # Create character
# new_character = create_character()

# # Save character to JSON file
# filename = input("Enter filename to save character (e.g., character): ") + ".json"
# while check_existing_file(filename):
#     print(f"Warning: A file with the name '{filename}' already exists. Please choose another name.")
#     filename = input("Enter filename to save character (e.g., character): ") + ".json"
# save_to_json(new_character, filename)

# print(f"Character {new_character.name} has been saved to {filename}")




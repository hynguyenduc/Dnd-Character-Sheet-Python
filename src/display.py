import json

"""
Import the json module to load and read json files in the directory
"""

def display_character_info(filename):
    """
    Opens the selected json file (i.e. filename) as a read only format and dispalys the information within

    Displays as:
        Name: xxx
        Race: xxx
        Strength: xx
        Dexterity: xx
        Constitution: xx
        Intelligence: xx
        Wisdom: xx
        Charisma: xx

    Except is there for error handling and debugging purposes 

    """
    try:
        with open(filename, 'r') as file:
            character_info = json.load(file)
            print("Character Information:")
            for key, value in character_info.items():
                print(f"{key.capitalize()}: {value}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.") # For debugging purposes


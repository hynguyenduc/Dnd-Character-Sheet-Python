import json

def display_character_info(filename):
    try:
        with open(filename, 'r') as file:
            character_info = json.load(file)
            print("Character Information:")
            for key, value in character_info.items():
                print(f"{key.capitalize()}: {value}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
# filename = input("Enter the filename of the character JSON file: ")
# display_character_info(filename)
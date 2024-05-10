import os, selector, display, create, json, delete
from create import Character, Character_choice


save_files = [file for file in os.listdir() if file.endswith(".json")]
selection = None
global filename
while selection != "iquit":
    print("Welcome to the DND character sheet app!")
    print("It stores up to 5 characters, keeps track of your character's stats and lets you make d20 rolls!")
    print("0. Add a new character!")
    selector.list_characters()
    print("000. Delete a saved character")
    print("Type 'iquit' to exit program")
    selection = input("Select by typing number in front of option then enter: ")
    try: 
        # Character Creator
        if selection == "0":
            if len(selector.get_character_files()) >= 5:
                print("You have 5 characters, please delete some to make space")
                confirmation = input("Input anything to go back to Main Menu")
                pass
            else:
                # Create character
                print("Let's create a new D&D character!")
                new_character = create.create_character()
                print(new_character.__dict__)
                # Save character to JSON file
                filename = input("Enter filename to save character (e.g., character): ") + ".json"
                while create.check_existing_file(filename):
                    print(f"Warning: A file with the name '{filename}' already exists. Please choose another name.")
                    filename = input("Enter filename to save character (e.g., character): ") + ".json"
                create.save_to_json(new_character, filename)
                print(f"Character {new_character.name} has been saved to {filename}")
                break  
        # Character delete
        elif selection == "000":
            print('Profile Delete')
            selector.list_characters()
            selection = input("Which one to delete?") 
            profiles = selector.get_character_files()
            filename = profiles[int(selection)-1][1]
            double_check = input("Are you sure? (Y/N): ")
            if double_check == "Y" or double_check == "y":
                print(f"File '{filename}' deleted successfully.")
                delete.delete_character_file(filename)
            elif double_check == "N" or double_check == "n": # need to fix this
                pass

        # Checks if input number equals existing file save number
        elif int(selection) <= len(save_files):
            profiles = selector.get_character_files()
            filename = profiles[int(selection)-1][1]
            break
            
        elif int(selection) < 0 or int(selection) > len(save_files):
            print("Please enter a valid selection number")

    except (ValueError, IndexError):    
        if selection == "iquit":
            print("To be continued! Thank you!")
        else:
            print("Please enter a valid selection number")

try:
    selection_input = None
    while selection_input != "iquit":
        display.display_character_info(filename)

        with open(filename) as f:
            dnd_data = json.load(f)

        print('Press (1) to edit character      Press (2) for character select\nPress (3) for a Strength roll       Press (4) for a Dexterity roll')
        print('Press (5) for a Constution roll      Press (6) for a Intelligence roll\nPress (7) for a Wisdom roll      Press (8) for a Charisma roll')
        selection_input = input('What do you want to do?: ')
        
        if int(selection_input) == 1:
            print("Character Editor")
            edit_character = create.create_character()
            delete.delete_character_file(filename) 
            filename = input("Enter filename to save character (e.g., character): ") + ".json"
            while create.check_existing_file(filename):
                print(f"Warning: A file with the name '{filename}' already exists. Please choose another name.")
                filename = input("Enter filename to save character (e.g., character): ") + ".json"
            create.save_to_json(edit_character, filename)
            print(f"Character {edit_character.name} has been saved to {filename}")


        elif int(selection_input) in range(3, 9):
            dnd_data.update({'player_input': int(selection_input)})
            select_choice = dnd_data.values()
            
            character = Character_choice(*select_choice)
            original_result, modified_result, modifier = character.roll_dice()
            print(f"Insert stat when needed: You rolled: {modifier}, original dice roll : {original_result}, , modifier added: {modified_result}")
            
            quit = input('Continue? (Y/N): ')
            if quit == 'N' or quit == 'n':
                print('Thanks for playing')
                break
            elif quit == 'Y' or quit == 'y':
                pass


except NameError:
    pass






# race attributes, and race to the json file name
# max point value for stats?
# bash scripting for app loading
# Fourth package? already using json, os, random

# limited save files?
# dice
# edit
# delete
        

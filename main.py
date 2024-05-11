import os, selector, display, create, json, delete
from create import Character, Character_choice

save_files = [file for file in os.listdir() if file.endswith(".json")]
# For the while loop for the main menu/character select
selection = None
# Makes the filename a global variable for easier code reference, when theres reassignment on a local level
global filename
# For the while loop for the character display menu to return to the main menu/character select
return_menu = False
try:
    while return_menu == False:
        return_menu = False
        while selection != "iquit":
            # Main Menu / Character Select intro with nagivation options
            print("Welcome to the DND character sheet app!")
            print("It stores up to 5 characters, keeps track of your character's stats and lets you make d20 rolls!")
            print("0. Add a new character!")
            # Prints list of existing characters
            selector.list_characters()
            print("000. Delete a saved character")
            print("Type 'iquit' to exit program")
            selection = input("Select by typing number in front of option then enter: ")
            # Try due to non integer selection variables raising a value error
            try: 
                # Character Creator code
                if selection == "0":
                    #Checks if you have too many save files
                    if len(selector.get_character_files()) >= 5:
                        print("You have 5 characters, please delete some to make space")
                        confirmation = input("Input anything to go back to Main Menu")
                        print()
                        pass
                    else:
                        # Create character
                        print("Let's create a new D&D character!")
                        new_character = create.create_character()
                        character_dict = new_character.__dict__
                        # Saves character to JSON as "(character name) the (race)"
                        filename = (f"{character_dict['name']} the {character_dict['race']}.json")
                        # Checks for duplicate save file names, lets you rename it
                        while create.check_existing_file(filename):
                            print(f"Warning: A file with the name '{filename}' already exists.")
                            print("Saved as 'another {filename}'")
                            filename = (f"another {filename}.json")
                        create.save_to_json(new_character, filename)
                        print(f"Character {new_character.name} has been saved")
                        break  
                
                # Character delete code
                elif selection == "000":
                    # Checks for valid input
                    profiles = selector.get_character_files()
                    if profiles == []:
                        print("No saved characters to delete")
                    else: 
                        while int(selection) != range(1, len(profiles)):    
                            print("Profile Delete")
                            selector.list_characters()
                            try:
                                selection = input("Which one to delete? ") 

                                if int(selection) > len(profiles) or int(selection) <= 0:
                                    print("There is no profile to delete!")
                                    print()
                                else:
                                    filename = profiles[int(selection)-1][1]
                                    break
                            except ValueError:
                                selection = 0
                                print("Please enter a valid selection number")
                                print()
                        # Double checks if you want to delete 
                        filename_wo_json = filename[:-5]
                        placeholder = True
                        while placeholder == True:
                            double_check = input(f"Are you sure you want to delete {filename_wo_json}? (Y/N): ")
                            if double_check == "Y" or double_check == "y":
                                print(f"File '{filename}' deleted successfully.")
                                placeholder = False
                                delete.delete_character_file(filename)
                            elif double_check == "N" or double_check == "n": 
                                print("Return to Main Menu")
                                placeholder = False
                            else:
                                print("Please enter a valid selection number")
                # Checks if input number equals existing file save number and leads to the display menu
                elif int(selection) <= len(save_files):
                    profiles = selector.get_character_files()
                    filename = profiles[int(selection)-1][1]
                    break
                # Checks if input was within the right values          
                elif int(selection) < 0 or int(selection) > len(save_files):
                    print("Please enter a valid selection number")
            # Raises NameError to exit the program from any menu (main/display)
            except (ValueError, IndexError):    
                if selection == "iquit":
                    print("To be continued! Thank you!")
                    raise NameError
                else:
                    print("Please enter a valid selection number")
        
        # Display menu section
        selection_input = None
        # while loop for program exit function
        while selection_input != "iquit":
            try:
                # Displays the characters stats for user reference
                display.display_character_info(filename)
                # Access the related json file for later manipulation
                with open(filename) as f:
                    dnd_data = json.load(f)
                # Prints possible inputs for user reference
                print("Press (1) to edit character      Press (2) for Main Menu/Character Select")
                print("Press (3) for a Strength roll       Press (4) for a Dexterity roll")
                print("Press (5) for a Constution roll      Press (6) for a Intelligence roll")
                print("Press (7) for a Wisdom roll      Press (8) for a Charisma roll")
                print("Press (iquit) to exit program")
                selection_input = input("What do you want to do?: ")
                print()
                
                # Character editor
                if int(selection_input) == 1:
                    print("Character Editor")
                    edit_character = create.create_character()
                    delete.delete_character_file(filename)
                    character_dict = edit_character.__dict__
                    filename = (f"{character_dict['name']} the {character_dict['race']}.json")
                    while create.check_existing_file(filename):
                        print(f"Warning: A file with the name '{filename}' already exists.")
                        print("Saved as 'another {filename}'")
                        filename = (f"another {filename}.json")
                    create.save_to_json(edit_character, filename)
                    print(f"Character {edit_character.name} has been saved")

                # Breaks the loop to return to main menu
                elif int(selection_input) == 2:
                    break

                # Makes the relevant dice roll
                elif int(selection_input) in range(3, 9):
                    dnd_data.update({"player_input": int(selection_input)})
                    select_choice = dnd_data.values()                    
                    character = Character_choice(*select_choice)
                    original_result, modifier, modified_result, stat_used = character.roll_dice()
                    print(f"{stat_used} ROLL: You rolled: {modified_result}, original dice roll : {original_result}, , modifier added: {modifier}")

                    read_result = input("The dice was rolled, hopefully in your favour. Press anything to continue")
                    print()
                # In case of wrong input
                else:
                    print("Please enter a valid selection number")
                    
                # for exiting program from the display menu
            except ValueError:
                if selection_input == "iquit":
                    print("To be continued! Thank you!")
                    raise NameError

                else:
                    print("Please enter a valid selection number")

# raises NameError to exit program 
except NameError:
    pass










import os, selector, display, create, dice, json
from dice import Character


print("Welcome to the character select page!")
print('0. Create a new character!:')
selector.list_characters()
save_files = [file for file in os.listdir() if file.endswith(".json")]
selection = None
global filename
while selection != "iquit":
    selection = input("Select by typing number infront of option then enter: ")
    try: 
        if selection == "0":
            # Create character
            new_character = create.create_character()
            # Save character to JSON file
            filename = input("Enter filename to save character (e.g., character): ") + ".json"
            while create.check_existing_file(filename):
                print(f"Warning: A file with the name '{filename}' already exists. Please choose another name.")
                filename = input("Enter filename to save character (e.g., character): ") + ".json"
            create.save_to_json(new_character, filename)
            print(f"Character {new_character.name} has been saved to {filename}")
            break  
        
        
        elif int(selection) <= len(save_files):
            profiles = selector.get_character_files()
            filename = profiles[int(selection)-1][1]
            break
            
        
        elif int(selection) > len(save_files):
            print("Sorry, there was no save file")
    except ValueError:    
        if selection == "iquit":
            print("To be continued! Thank you!")
        else:
            print("Please enter a valid response")

try:
    display.display_character_info(filename)

    with open(filename) as f:
        dnd_data = json.load(f)
    print(dnd_data)

    print('Press (1) to edit character\nPress (2) for character select\nPress (3) for a Strength roll\nPress (4) for a Dexterity roll')
    print('Press (5) for a Constution roll\nPress (6) for a Intelligence roll\nPress (7) for a Wisdom roll\nPress (8) for a Charisma roll')
    selection_input = input('What do you want to do?:')
    
    role_tuple = [(3, 'Strength'), (4, 'Dexterity'), (5, 'Intelligence')]
    

    character = Character()
    for index in role_tuple:
        if role_tuple[index] == int(selection_input): 
            original_result, modified_result, modifier = character.roll_dice()
            print(f"{stat}: Original Roll Result: {original_result}, Modifier Used: {modifier}, Modified Result: {modified_result}")

except NameError:
    pass



# if __name__ == "__main__":


# edit
# delete
# dice
# race attributes
# max point value for stats?
# bash scripting for app loading


        

import os, selector, display, create


print("Welcome to the character select page!")
print('0. Create a new character!:')
selector.list_characters()
save_files = [file for file in os.listdir() if file.endswith(".json")]
selection = None
while selection != "iquit":
    selection = input("Select by typing front number then enter: ")
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
        elif int(selection) <= len(save_files):
            profiles = selector.get_character_files()
            profile_num = profiles[int(selection)-1][1]
            display.display_character_info(profile_num)      
        elif int(selection) > len(save_files):
            print("Sorry, there was no save file")
    except ValueError:    
        if selection == "iquit":
            print("To be continued! Thank you!")
        else:
            print("Please enter a valid response")

# if __name__ == "__main__":



        

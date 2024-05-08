import os, selector, display


print("Welcome to the character select page!")
print('0. Create a new character!:')
selector.list_characters()
save_files = [file for file in os.listdir() if file.endswith(".json")]
selection = None
while selection != "iquit":
    selection = input("Select by typing front number then enter: ")
    try: 
        if selection == "0":
            import create
            create.create_character()   
        elif int(selection) <= len(save_files):
            display.display_character_info(selector.link_characters)
        elif int(selection) > len(save_files):
            print("Sorry, there was no save file")
    except ValueError:    
        if selection == "iquit":
            print("To be continued! Thank you!")
        else:
            print("Please enter a valid response")

# if __name__ == "__main__":



        

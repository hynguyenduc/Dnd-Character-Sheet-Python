import create
import os

def list_characters():
    json_files = [file for file in os.listdir() if file.endswith(".json")]
    print("Available Characters:")
    if json_files == []:
        print("No saved characters")
    for idx, filename in enumerate(json_files, 1):
        print(f"{idx}. {filename[:-5]}")  # Print filename without the ".json" extension

selection = None
print("Welcome to the character select page!")
print('0. Create a new character!:')
list_characters()
while selection == None:
    selection = input("Select by typing front number then enter:")
    if selection == "0":
        
    

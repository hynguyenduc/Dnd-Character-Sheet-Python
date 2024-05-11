import os, json

"""
Uses os module to access the directory
Uses json module read, load and edit json files
"""

def list_characters():
    """
    Looks at the directory for any pre-existing json files which hold character information (aka a save file)
    
    If there are no json files, then it displays 'No saved characters'

    If there are any json files, then it displays the json files in a numbered list
    """
    json_files = [file for file in os.listdir() if file.endswith(".json")]
    print("Available Characters:")
    if json_files == []:
        print("No saved characters") # Prompt if there are no saved characters
    for idx, filename in enumerate(json_files, 1):
        print(f"{idx}. {filename[:-5]}")  # Print filename without the ".json" extension

def get_character_files(directory="."):
    """
    Looks in directory and returns a list of character files (files that end with .json)

    Returns a list of character files to be iterated through
    """
    json_files = [file for file in os.listdir(directory) if file.endswith(".json")]
    return [(idx, filename) for idx, filename in enumerate(json_files, 1)]    

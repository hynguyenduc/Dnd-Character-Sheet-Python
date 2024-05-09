import os, json

def list_characters():
    json_files = [file for file in os.listdir() if file.endswith(".json")]
    print("Available Characters:")
    if json_files == []:
        print("No saved characters")
    for idx, filename in enumerate(json_files, 1):
        print(f"{idx}. {filename[:-5]}")  # Print filename without the ".json" extension

def get_character_files(directory="."):
    json_files = [file for file in os.listdir(directory) if file.endswith(".json")]
    return [(idx, filename) for idx, filename in enumerate(json_files, 1)]    

# def get_character_files(directory="."):
#     json_files = [file for file in os.listdir(directory) if file.endswith(".json")]
#     return [{idx : filename} for idx, filename in enumerate(json_files, 1)]
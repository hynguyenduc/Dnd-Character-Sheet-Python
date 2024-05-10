import os
from os import system, name


def delete_character_file(filename):
    try:
        os.remove(filename)
        # print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

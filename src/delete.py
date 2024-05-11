import os

"""
Uses the os module to access directory
"""

def delete_character_file(filename):
    """
    Deletes the selected json file (saved under variable filename) from the directory permanently.

    Except used for debugging purposes
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

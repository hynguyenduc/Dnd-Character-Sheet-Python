import os, json, random

"""
    Imports os module to scan the directory
    Imports json module to load, read and edit json files in the directory
    Imports random module for the dice roll
"""


class Character:
    """
    Creates a character

    Parameters:
    -----------
    name 
    race 
    strength
    dexterity
    constution
    intelligence
    wisdom
    charisma

    """
    def __init__(self, name, race, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

class Character_choice(Character):
    """
    Inherits the parameters from character but adds extra parameter called select_choice

    Select_choice is used as a way to select the options displayed on the character display menu

    It is added onto the end of the character class
    """
    def __init__(self, name, race, strength, dexterity, constitution, intelligence, wisdom, charisma, select_choice):
        super().__init__(name, race, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.select_choice = select_choice

    
    def roll_dice(self):
        """
        Uses the imported random module from the standard library

        returns a psuedo random number generated between 1-20
        returns the modifier used based on select_choice
        returns the modified result (roll plus modifier)
        returns the name of the stat roll e.g. if it was a stength roll, will return string 'STR'
        """
        roll = random.randint(1, 20)
        modifier, stat_used = self.get_modifier()
        modified_result = roll + modifier
        return roll, modifier, modified_result, stat_used
        

    def get_modifier(self):
        """
        Matches the select_choice attribute to corresponding stat (the numbers are choosen based on the display menu)

        Returns the corresponding modifier and stat name

        """
        modifiers = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1,
            10: 0, 11: 0, 12: +1, 13: +1, 14: +2, 15: +2, 16: +3, 17: +3, 18: +4, 19: +4, 20: +5
        }
        stats = [(3, self.strength, "STR"), (4, self.dexterity, "DEX"), (5, self.constitution, "CON"), (6, self.intelligence, "INT"), (7, self.wisdom, "WIS"), (8, self.charisma, "CHA")]
        for stat in range(len(stats)):
            if stat+3 == self.select_choice:
                # modifier used
                modifier = modifiers[stats[stat][1]] 
                # name of stat roll
                stat_used =  stats[stat][2] #
        return modifier, stat_used



def create_character():
    """
    Takes in inputs for character stats

    Used while loops for each stat to prevent unrelated input forms 
    i.e. stats can only be integers
    
    """
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    strength=dexterity=constitution=intelligence=wisdom=charisma = None
    while strength != int:
        try:
            strength = int(input("Enter character strength (1-20): "))
            if strength <= 0 or strength > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue
    while dexterity != int:
        try:
            dexterity = int(input("Enter character dexterity (1-20): "))
            if dexterity <= 0 or dexterity > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue
    while constitution != int:
        try:
            constitution = int(input("Enter character constitution (1-20): "))
            if constitution <= 0 or constitution > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue      
    while intelligence != int:
        try:
            intelligence = int(input("Enter character intelligence (1-20): "))
            if intelligence <= 0 or intelligence > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue  
    while wisdom != int:
        try:
            wisdom = int(input("Enter character wisdom (1-20): "))
            if wisdom <= 0 or wisdom > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue  
    while charisma != int:
        try:
            charisma = int(input("Enter character charisma (1-20): "))
            if charisma <= 0 or charisma > 20:
                raise KeyError
            else:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        except KeyError:
            print("Please enter a number between 1 and 20")
            continue  
    return Character(name, race, strength, dexterity, constitution, intelligence, wisdom, charisma)


def save_to_json(character, filename):
    """
    Takes the character attributes user inputs and saves them to a json file
    """
    with open(filename, 'w') as file:
        json.dump(vars(character), file, indent=4)

def check_existing_file(filename):
    """ 
    Checks directory for json file with same name to prevent unexpected overwriting
    """
    return os.path.isfile(filename)





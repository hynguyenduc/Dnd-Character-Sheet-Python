import os, json, random

class Character:
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
    def __init__(self, name, race, strength, dexterity, constitution, intelligence, wisdom, charisma, select_choice): #):
        super().__init__(name, race, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.select_choice = select_choice

    
    def roll_dice(self):
        # Roll a 20-sided dice (D20) and add the character's relevant ability modifier
        roll = random.randint(1, 20)
        modifier = self.get_modifier()
        modified_result = roll + modifier
        return roll, modifier, modified_result
        

    def get_modifier(self):
        # Calculate the ability modifier based on the ability score
        modifiers = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1,
            10: 0, 11: 0, 12: +1, 13: +1, 14: +2, 15: +2, 16: +3, 17: +3, 18: +4, 19: +4, 20: +5
        }
        stats = [(3, self.strength), (4, self.dexterity), (5, self.constitution), (6, self.intelligence), (7, self.wisdom), (8, self.charisma)]
        for stat in range(len(stats)):
            if stat+3 == self.select_choice:
                modifier = modifiers[stats[stat][1]] 
        return modifier



def create_character():
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
    with open(filename, 'w') as file:
        json.dump(vars(character), file, indent=4)

def check_existing_file(filename):
    return os.path.isfile(filename)





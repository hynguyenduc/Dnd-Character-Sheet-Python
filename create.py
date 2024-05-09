import os, json, random

class Character:
    def __init__(self, name, race, strength, dexterity, constitution):
        self.name = name
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

class Character_choice(Character):
    def __init__(self, name, race, strength, dexterity, constitution, select_choice): #, intelligence, wisdom, charisma):
        super().__init__(name, race, strength, dexterity, constitution)
        self.select_choice = select_choice
        # self.intelligence = intelligence
        # self.wisdom = wisdom
        # self.charisma = charisma
    
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
        stats = [(3, self.strength), (4, self.dexterity), (5, self.constitution)]
        for stat in range(len(stats)):
            if stat+3 == self.select_choice:
                modifier = modifiers[stats[stat][1]] 
        return modifier



def create_character():
    name = input("Enter character name: ")
    race = input("Enter character race: ")
    strength = int(input("Enter character strength: "))
    dexterity = int(input("Enter character dexterity: "))
    constitution = int(input("Enter character constitution: "))
    return Character(name, race, strength, dexterity, constitution)

def save_to_json(character, filename):
    with open(filename, 'w') as file:
        json.dump(vars(character), file, indent=4)

def check_existing_file(filename):
    return os.path.isfile(filename)





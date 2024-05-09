import random

class Character:
    def __init__(self, name, strength, dexterity): #, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        # self.constitution = constitution
        # self.intelligence = intelligence
        # self.wisdom = wisdom
        # self.charisma = charisma
    
    def roll_dice(self):
        # Roll a 20-sided dice (D20) and add the character's relevant ability modifier
        roll = random.randint(1, 20)
        modifier = self.get_modifier()
        modified_result = roll + modifier
        return roll, modifier, modified_result
        
    
    # Tabnine autofilled this --> could be useful later
    # def __str__(self):
    #     return f"Name: {self.name}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\n"

    def get_modifier(self):
        # Calculate the ability modifier based on the ability score
        modifiers = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1,
            10: 0, 11: 0, 12: +1, 13: +1, 14: +2, 15: +2, 16: +3, 17: +3, 18: +4, 19: +4, 20: +5
        }

        modifier = modifiers[self.strength]  # You can replace 'strength' with any other ability score
        return modifier

# # Example usage:
# character_name = input("Enter character name: ")
# character_strength = int(input("Enter character strength: "))
# character_dexterity = int(input("Enter character dexterity: "))
# # character_constitution = int(input("Enter character constitution: "))
# # character_intelligence = int(input("Enter character intelligence: "))
# # character_wisdom = int(input("Enter character wisdom: "))
# # character_charisma = int(input("Enter character charisma: "))

# # Create character object
# character = Character(
#     character_name, character_strength, character_dexterity
#     ) 
# # , character_constitution,
# #     character_intelligence, character_wisdom, character_charisma


# # Roll dice
# print("Rolling dice...")
# stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
# for stat in stats:
#     original_result, modified_result, modifier = character.roll_dice()
#     print(f"{stat}: Original Roll Result: {original_result}, Modifier Used: {modifier}, Modified Result: {modified_result}")

import pandas as pd
import numpy as np

#Variables 
House_Points = 150 
Welcome_Message = "Welcome To Hogwarts, Young Witch or Wizard"
Magical_Creatures = ["Hippogriff", "Thestral", "Niffler", "Phoenix", "Basilisk"]

Hogwarts_School_Supplies = {
    "wand": "Holly with Phoenix Feather Core",
    "spellbook": ["Expelliarmus", "Lumos", "Expecto Patronum"],
    "potions": {
        "Felix Felicis": 1,
        "Polyjuice Potion": 2,
        "Veritaserum": 3
    }
}

# Function for The Outcome of A Magic Duel 
def Magical_Duel(Spell_Power, Opponent_Strength):
    if Spell_Power > Opponent_Strength:
        return "You Casted An Amazing Spell and Win the Duel"
    elif Spell_Power < Opponent_Strength:
        return "Your opponent is too strong... You lose the duel."
    else:
        return "Both Wizarads Are Still Standing The Duel Ends In A Draw!"


# Print Variables
print("House Points:", House_Points)
print("Welcome Message:", Welcome_Message)
print("Magical Creatures:", Magical_Creatures)
print("Hogwarts School Supplies:", Hogwarts_School_Supplies)

# Example usage of the function
duel_result = Magical_Duel(70, 80)
print("Duel Result:", duel_result)


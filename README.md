# 506-Practice-Workflow
This repository is a primer for 504/507 Fall semester classes to practice a basic development workflow 

## Summary of Variables

- House_Points: An integer representing the total points earned by a Hogwarts house. In this case, it was set to `150`.
- Welcome_Message: A string containing a welcome message for the young witches and wizards at Hogwarts: "Welcome To Hogwarts, Young Witch or Wizard".
- Magical_Creatures: A list of magical creatures, including "Hippogriff", "Thestral", "Niffler", "Phoenix", and "Basilisk".
- Hogwarts_School_Supplies: A dictionary that contains:
  - wand: A string describing a wand with "Holly with Phoenix Feather Core".
  - spellbook: A list of spells including Expelliarmus, Lumos, and Expecto Patronum.
  - potions: A nested dictionary with potion names as keys and their quantities as values:
    - Felix Felicis: 1 dose.
    - Polyjuice Potion: 2 doses.
    - Veritaserum: 3 doses.

## Summary of the Function

The Python script contains a function named Magical_Duel that determines the outcome of a duel between two wizards based on their Spell_Power and Opponent_Strength.

### Function Logic

- If the wizard's Spell_Power is greater than the Opponent_Strength, the wizard wins the duel with a message: "You Casted An Amazing Spell and Win the Duel"`.
- If the wizard's Spell_Power is less than the Opponent_Strength, the wizard loses the duel with a message: "Your opponent is too strong... You lose the duel."
- If both powers are equal, the duel ends in a draw with the message: Both Wizarads Are Still Standing The Duel Ends In A Draw!

## Example Usage and Expected Output

Based on the function down below we should get a message stating: "Your Opponent Is Too Strong... You Lose The Duel."
duel_result = Magical_Duel(70, 80)
print("Duel Result:", duel_result)
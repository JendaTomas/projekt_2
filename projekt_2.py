"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jenda Tomáš
email: jenda.tomas@seznam.cz
discord: jendatomas
"""

import random
        

# conditions for number
def correct_entry():
    """
    kontroluje, zda zadané číslo splňuje podmínky
     
    """
    while True:
        global guess_number
        guess_number=input(">>> ")
        if len(guess_number) != 4 or not guess_number.isnumeric():
            print("The number you entered have to contain exactly 4 digits!")
            continue
        elif guess_number[0] == str(0):
            print("The number can not start with zero! ")
            continue
        elif guess_number.isnumeric() and len(set(guess_number)) != 4:  # poznámka pro mne: set vyřadí opakující se hodnoty -> když v 4 číslech je více stejných
            print("The number you entered have to contain 4 different digits!")   # čísel, jeho délka nebude 4
            continue                                                              
        else:
            break                                                                           

# number of bulls
def quantity_of_bulls_cows():
    """
    vyhodnocuje počet bulls a cows

    """
    global quantity_bulls
    global quantity_cows
    quantity_cows = 0
    quantity_bulls = 0
    for i in range(0,4):
        if int(guess_number[i])== int(random_number[i]):
            quantity_bulls += 1
        elif int(guess_number[i]) in random_number:
            quantity_cows += 1

# plural/singular nouns
def suffixword():
    """
    správná koncovka u jednotného a množného čísla

    """
    global name_bull
    global name_cow
    name_bull = "bulls"
    name_cow = "cows"
    if quantity_bulls == 1:
        name_bull = name_bull[:-1] 
    if quantity_cows == 1:
        name_cow= name_cow[:-1]

# the game
### greeting and introduction
line= 47*"-"
print(f"Hit there!\n{line}\n",
      "I´ve generated a random 4 digit number for you.\n",
      f"Let´s play a bulls and cows game.\n{line}\n",
      f"Enter a number:\n {line}\n")

### random "number"(list) generation
number= [0,1,2,3,4,5,6,7,8,9]
random_number=[0]
while random_number[0]==0:
    random_number= random.sample(number,4)
number_rounds = 0
quantity_bulls = 0
while quantity_bulls != len(random_number):
    number_rounds += 1
    correct_entry()
    quantity_of_bulls_cows()
    suffixword()
    print( f"{quantity_bulls} {name_bull}, {quantity_cows} {name_cow}")
else:
    print(f"""Correct, you´ve guessed the right number
in {number_rounds} guessed!\n{line}""")

'''
guessthenumber.py: Gissa nummer spel.

__author__  = "Oliver Stader"
__version__ = "1.0.0"
__email__   = "oliver.stalder@elev.ga.dbgy.se"
'''


import random

from bcolors import bcolors

print(bcolors.CYAN + "Välkommen till nummerspelet")
    

while True:

    number = random.randint(1, 100)

    guessnmr = 0

    while True:

        
        try:
            guess = int(input(bcolors.YELLOW + "Vilket nummer gissar du på?: "))

        except:
            print(bcolors.RED + "Skriv in ett heltal")

            continue


        if guess > number:
            guessnmr += 1
            if guessnmr == 7:
                print(bcolors.YELLOW + "Du förlorade, numret var", number)
                break
            else:
                print(bcolors.RED + "För stort, antal gissningar kvar är", 7 - guessnmr)
                

        elif guess < number:
            guessnmr += 1
            if guessnmr == 7:
                print(bcolors.YELLOW + "Du förlorade, numret var", number)
                break 

            else:
                print(bcolors.RED + "För litet, antal gissningar kvar är", 7 - guessnmr)
                
        else:
            print(bcolors.GREEN + "Grattis, du gissade rätt")
            break

    spelaigen = input(bcolors.YELLOW + "Vill du spela igen (J)a / (N)ej?: ")
    if spelaigen.upper() == "N":
        exit()

    else:
        continue
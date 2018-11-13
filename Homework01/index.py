# Rock-paper-scissors-lizard-Spock game

import random

def name_to_number(name):
    
    if name == "rock":
        number = 0
        print ("Player chooses rock")
    elif name == "Spock":
        number = 1
        print ("Player chooses Spock")
    elif name == "paper":
        number = 2
        print ("Player chooses paper")
    elif name == "lizard":
        number = 3
        print ("Player chooses lizard") 
    elif name == "scissors":
        number = 4
        print ("Player chooses scissors")
    else:
        print ("Wrong value!")
        
    return number

def number_to_name(number):
    
    if number == 0:
        name = "rock"
        print("Computer chooses rock")
    elif number == 1:
        name = "Spock"
        print("Computer chooses Spock")
    elif number == 2:
        name = "paper"
        print("Computer chooses paper")
    elif number == 3:
        name = "lizard"
        print("Computer chooses lizard")
    elif number == 4:
        name = "scissors"
        print("Computer chooses scissors")
    else:
        print("Wrong value!")
    
    return number

def rpsls(player_choice):
    
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    number_to_name(comp_number)
    winner_select = (comp_number - player_number)%5
    
    if winner_select == 1 or winner_select == 2:
        print ("Computer wins!\n")
    elif winner_select == 3 or winner_select == 4:
        print ("Player wins!\n")
    else:
        print ("It's a draw!\n")
    
    
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





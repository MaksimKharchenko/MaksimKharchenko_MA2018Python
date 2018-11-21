import simplegui
import random

guess = 0
secret_number = 0

def new_game():
    
    global secret_number
    secret_number = random.randrange(0, 100)
    print("A new game has started with a range from 0 to 100\n")
   
def input_guess(user_input):
    
    global guess
    guess = int(user_input)
    print "Guess was:", guess
    
    if guess == secret_number:
        print "Correct!\n"
    elif guess < secret_number:
        print "Higher!\n"
    elif guess > secret_number:
        print "Lower!\n"
        
def range100():
    
    new_game()
    
def range1000():
    
    global secret_number
    secret_number = random.randrange(0, 1000)
    print("A new game has started with a range from 0 to 1000\n")

frame = simplegui.create_frame("Guess the number", 200 ,200)
frame.add_input("Input guess", input_guess, 195)
frame.add_button("Range (0, 100)", range100, 200)
frame.add_button("Range (0, 1000)", range1000, 200)
frame.start()
new_game()

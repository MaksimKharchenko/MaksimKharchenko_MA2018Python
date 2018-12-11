# implementation of card game - Memory

import simplegui
import random
indent = 50
card_list = []
exposed = []
turns = 0
choices = [-1,-1]
# helper function to initialize globals

def new_game():
    
    global card_list, exposed, state, choices, turns
    list2 = card_list
    for i in range(8):
        card_list.append(i) 
    card_list.extend(list2)
    random.shuffle(card_list)
    exposed = [0] * 16
    state = 0
    turns = 0
    choices = [-1,-1]
    label.set_text("Moves = " + str(turns))
# define event handlers

def mouseclick(pos):
    
    # add game state logic here
    global state, turns, choices
    index = int(pos[0] / indent)
    if(state == 0):
        if(exposed[index] == 0):
            if(card_list[choices[0]] != card_list[choices[1]]):
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[index] = 1
            state = 1
            choices[0] = index
    elif state == 1:
        if(exposed[index] == 0):
            state = 0
            exposed[index] = 1
            choices[1] = index
            turns += 1   
            label.set_text("Moves = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size 

def draw(canvas):
    
    for i in range(16):
        if(exposed[i]==0):
            canvas.draw_polygon([(50*i, 0), (50*(i+1), 0), (50*(i+1), 100),(50*i, 100)],1,"black","green")
        else:
            canvas.draw_text(str(card_list[i]),[50*i+5,75], 70,"red")
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

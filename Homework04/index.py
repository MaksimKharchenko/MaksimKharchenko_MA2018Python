# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
score1 = 0
score2 = 0
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = 160
paddle2_pos = 160
paddle1_vel = 0
paddle2_vel = 0
vel = 6
# initialize ball_pos and ball_vel for new bal in middle of table

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 5)
        ball_vel[1] = -random.randrange(1, 4)
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(2, 5)
        ball_vel[1] = -random.randrange(1, 4)
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    first_move = random.randrange(1, 3)
    if first_move == 1:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # collide and reflect off of top and bottom of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) or ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):        
        ball_vel[0] = - ball_vel[0]
        
        if (ball_pos[0] > WIDTH / 2):             
            if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + PAD_HEIGHT):
                score1 += 1 
                spawn_ball(LEFT) 
            else: ball_vel[0] +=  ball_vel[0] * 0.1
            
        if (ball_pos[0] < WIDTH / 2):
            if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + PAD_HEIGHT ):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] +=  ball_vel[0] * 0.1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    #draw scores
    
    canvas.draw_text(str(score1), (150, 50), 40, "Red")
    canvas.draw_text(str(score2), (450, 50), 40, "Red")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel  
    # draw paddles
    #left
    canvas.draw_polygon([(0, paddle1_pos), (8, paddle1_pos), (8,  paddle1_pos + 80), (0,  paddle1_pos + 80)], 1, 'Blue', 'White')
    #right
    canvas.draw_polygon([(592, paddle2_pos), (600, paddle2_pos), (600, paddle2_pos + 80), (592, paddle2_pos + 80)], 1, 'Blue', 'White')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel     
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel  
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel
   
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

        
def restart_button():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart_button, 100)

# start frame
new_game()
frame.start()


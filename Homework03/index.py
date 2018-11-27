import simplegui

interval = 100
t = 0
position = [100, 100]
score_position = [230, 30]
message = '0:00.0'
games = 0
wins = 0
timer_running = 0

def time():
    
    global t
    t += 1
    format(t) 
    
def draw(canvas):
    score = str(wins) + '/' +str(games)
    canvas.draw_text(message, position, 35, "Yellow")
    canvas.draw_text(score, score_position, 20, "Red")
    
def start_button():
    global timer_running
    timer_running = 1
    timer.start()
    
def stop_button():
    
    global wins, games, timer_running
    timer.stop()
    games = games + timer_running
    if message[5] == '0' and timer_running:
        wins += 1
    timer_running = 0
    
def reset_button():
    
    timer.stop()
    global t, games, wins
    t = 0
    games = 0
    wins = 0
    format(t)
    
def format(t):
    
    global message
    tenth_of_seconds = t % 10
    interim = (t - tenth_of_seconds) / 10
    seconds = interim % 60
    minutes = interim // 60
    if seconds >=10:
        message = str(minutes) + ':' + str(seconds) + '.' +str(tenth_of_seconds)
    else:
        message = str(minutes) + ':0' + str(seconds) + '.' +str(tenth_of_seconds)    

        
frame = simplegui.create_frame("Timer", 300, 200)
frame.set_draw_handler(draw)
frame.add_button('Start', start_button, 100)
frame.add_button('Stop', stop_button, 100)
frame.add_button('Reset', reset_button, 100)
                                                                
timer = simplegui.create_timer(interval, time)

frame.start()

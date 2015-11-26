# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
total_clicks = 0
player_score = 0
t_running = True
message = "timer text"
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    mseconds = counter % 10
    rem_time = counter // 10
    minutes = rem_time // 60
    seconds = rem_time % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
        
    
    message = str(minutes) + ":" + str(seconds) + ":" + str(mseconds)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global t_running 
    t_running = True
    timer.start()
    
    
def stop():
    global total_clicks, score, player_score, t_running
    
    if t_running:
        
        timer.stop()
        total_clicks += 1 
    
        if counter % 10 == 0:
            player_score += 1
    else:
        timer.stop()
        if counter % 10 == 0:
            print "No cheating! Press start to continue :)"
        else:
            print "Press start to continue game"
        
               
    score = str(player_score) + "/" + str(total_clicks)
    
    t_running = False
    
        
def reset():
    global counter, total_clicks, player_score, score
    timer.stop()
    counter = 0
    total_clicks = 0
    player_score = 0
    score = "0/0"

# define event handler for timer with 0.1 sec interval
def tick():
    global counter, message
    counter += 1
    
      

# define draw handler
def draw(canvas):
    global counter, message, score
    format(counter)
    canvas.draw_text(message, [45, 90], 45, "White")
    canvas.draw_text(score, [150, 20], 20, "Grey")
    
    
    
# create frame
frame = simplegui.create_frame("Stop watch game", 200, 150)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric

# implementation of card game - Memory

import simplegui
import random

turns = 0
posn = [0,0]


# helper function to initialize globals
def new_game():
    global memory_deck, opened_deck, flip_state, turns, exposed
    list1 = range(8)
    list2 = range(8)
    memory_deck = list1 + list2
    random.shuffle(memory_deck)
    
    exposed=[False for i in range(16)]
    
    opened_deck = []
    flip_state = 0
    turns = 0
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global flip_state, turns, posn
    posn = pos
    
    if flip_state == 0:
        
        opened_deck.append(pos[0]//50)
        exposed[pos[0]//50]=True        
        
        flip_state = 1
        turns = 1
        
    elif flip_state == 1:
        
        if not (pos[0]//50 in opened_deck):
            opened_deck.append(pos[0]//50)     
        
        flip_state = 2
        
        exposed[pos[0]//50]=True
        
    else:
        
         if not (pos[0]//50 in opened_deck):
            if memory_deck[opened_deck[-1]]!=memory_deck[opened_deck[-2]]:
                
                exposed[opened_deck[-1]]=False
                exposed[opened_deck[-2]]=False
                opened_deck.pop()
                opened_deck.pop()
                
            flip_state = 1
            turns +=1
            
            exposed[pos[0]//50]=True
            opened_deck.append(pos[0]//50)
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
        global posn
        label.set_text("Turns = "+str(turns))
        for i in range(16):
            canvas.draw_line([50*(i%15+1),0], [50*(i%15+1),100], 2, "Black")
            if exposed[i]:
                #simplyfy the black bg! messing up the expose
                #canvas.draw_polygon([[posn[0]//50*50, posn[1]//100*50],[posn[0]//50*50 + 50, posn[1]//100*50],[posn[0]//50*50 + 50, posn[1]//100*50 + 100],[posn[0]//50*50, posn[1]//100 + 100]], 2, "Black", "Black")
                
                canvas.draw_text(str(memory_deck[i]), [15+50*i,70], 50, "White")
         

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
frame.set_canvas_background('Green')
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
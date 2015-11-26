# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""

score = 0
deck = []
dealer = []
player = []



# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class ##tested
class Hand:
    def __init__(self):
        
        # create Hand object
        self.hand = []
                    
    def __str__(self):
        # return a string representation of a hand       
        return ','.join([card.get_suit()+card.get_rank() for card in self.hand])
   
    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        
        hand_value = 0
        ace = 0
        for card in self.hand:
            hand_value += VALUES.get(card.get_rank())
            if card.get_rank() == "A":
                ace += 1
        if ace > 0 and hand_value + 10 <= 21:
            hand_value + 10
        return hand_value
            
        
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        
        x = 0
        
        for card in self.hand:
            
            card.draw(canvas, [pos[0]+x, pos[1]])
            x += 80
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s,r))
                
        self.shuffle()

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        return ' '.join([card.get_suit()+card.get_rank() for card in self.deck])



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, score
   
    # your code goes here
    outcome = "Hit or Stand?"
    deck = Deck()
    player = Hand()
    dealer = Hand()
    
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    #print "Dealer has "+str(dealer)+" with the value of "+str(dealer.get_value())
    #print "Player has "+str(player)+" with the value of "+str(player.get_value())
    
    in_play = True

def hit():

    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global in_play, outcome, score, player, dealer
    
    if in_play == True:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            
            if player.get_value() == 21:
                outcome = "You have a Blackjack! New Deal?"
                score += 1
                
            elif player.get_value() >21:
                outcome = "Busted! Loser. New Deal?"
                in_play = False
                score -= 1
    else:
        #error 
        outcome = "You got no hit!"
        
        
       
def stand():
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global player, dealer, score, outcome, in_play
    
    if in_play == True:
        if player.get_value() > 21:
            outcome = "You're still busted!"
            
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            if dealer.get_value() > 21:
                outcome = "Dealer got Busted!! New Deal?"
                score += 1
                
            elif dealer.get_value() > player.get_value():
                outcome = "Dealer won :( .New Deal?"
                score -= 1
                
            elif dealer.get_value() == player.get_value():
                outcome = "Tie! errr Dealer wins. New Deal?"
                score -= 1
        
            elif dealer.get_value() < player.get_value():
                outcome = "You won!!! New Deal?"
                score += 1
                
    in_play = False
    #outcome = "New deal?"               
    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, card_back
    
    canvas.draw_text("Score: "+str(score), (400, 100), 26, "Black")
    canvas.draw_text("Blackjack", (70,100), 38, "Blue")
    canvas.draw_text("Dealer", (70, 180), 26, "Black")
    canvas.draw_text(outcome, (220, 180), 26, "Black")
    canvas.draw_text("Player", (70, 380), 26, "Black")
    
       #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    dealer.draw(canvas, [50,200])
    player.draw(canvas, [50,400])
    #card = Card("S", "A")
    if in_play == True:
        canvas.draw_image(card_back, [35.5, 48], [71,96], [85.5,248], [71,96])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
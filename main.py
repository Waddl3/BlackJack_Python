from logo import logo
from Blackjack import random, display, drawCard

# Given:
print(logo); # Logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] # deck of cards
starter = 0

user_card  = []
user_total = 0
dealer_card = []
dealer_total = 0
_continue = True

# 2 cards
while starter < 2:
    uRandom = random.choice(cards)
    user_card.append(uRandom)
    user_total += uRandom
    
    dRandom = random.choice(cards)
    dealer_card.append(dRandom)
    dealer_total += dRandom
    
    starter += 1

display(userCards=user_card, dealerCards=dealer_card)

# check if either one has blackjack (21)
if user_total == 21 or dealer_total == 21:
    if dealer_total == 21:
        print("Dealer Wins")
        _continue = False
    else: 
        user_total == 21
        print("User Wins!")
        _continue = False
        
while _continue:
    dChoice = random.randint(0, 1)
    
    uChoice = input("Draw card ('d') or Stay('s')? ")
    if uChoice.lower() == 'd':
        drawn = new_card = random.choice(cards)
        user_total, user_card = drawCard(total=user_total, player=user_card, new_card=drawn) 
        display(userCards=user_card, dealerCards=dealer_card)
    elif uChoice.lower() == 's':    # Once player is done drawing
        while dealer_total < 17:
            drawn = new_card = random.choice(cards)
            dealer_total, dealer_card = drawCard(total=dealer_total, player=dealer_card, new_card=drawn)
    
    if user_total > 21:
        print("Dealer Wins!")
        _continue = False;
    elif dealer_total > 21:
        print("User Wins!")
        _continue = False
    
        



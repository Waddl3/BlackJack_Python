import random

def display(userCards, dealerCards):
    print("User's Hand: " + str(userCards))
    
    dealer = "Dealer's Hand: "
    for card in range (len(dealerCards) - 1):
        dealer += str(dealerCards[card])
    
    print(dealer)

def isAce(drawn):
    return drawn == 11

def drawCard(total, player, new_card):
        player.append(new_card)
        total += new_card
        return total, player

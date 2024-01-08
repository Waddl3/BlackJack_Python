import random

def display(user_cards, dealer_cards, dealer_hide=False):
    """Display user's and dealer's hands."""
    print("User's Hand:", user_cards)
    if dealer_hide:
        print("Dealer's Hand:", dealer_cards[0], "<hidden card>")
    else:
        print("Dealer's Hand:", dealer_cards)

def draw_card(total, player, new_card):
    """Add a new card to a player's hand and update the total."""
    player.append(new_card)
    total += new_card
    return total, player

def is_blackjack(total, size):
    """Check if a player has a natural Blackjack."""
    return total == 21 and size == 2

def check_winner(user, dealer):
    """Check and declare the winner."""
    if user > 21:
        return "Dealer"
    elif dealer > 21:
        return "Player"
    elif user > dealer:
        return "Player"
    elif dealer > user:
        return "Dealer"
    else:
        return "Tie"

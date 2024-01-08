from logo import logo
import Blackjack, random

print(logo)  # Display logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]  # Deck of cards

user_cards = []
dealer_cards = []
game_over = False

# Deal initial cards
for _ in range(2):
    user_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

# Display initial hands
Blackjack.display(user_cards, dealer_cards, dealer_hide=True)

# Check for initial Blackjack
if Blackjack.is_blackjack(sum(user_cards), len(user_cards)):
    print("You have a natural Blackjack! You win!")
    game_over = True
        
while not game_over:
    user_choice = input("Do you want to draw another card? ('y' or 'n'):").lower()
    
    if user_choice == 'y':
        new_card = random.choice(cards)
        total, user_cards = Blackjack.draw_card(sum(user_cards), user_cards, new_card)
        Blackjack.display(user_cards, dealer_cards, dealer_hide=True)
        
        if total > 21:
            print("You busted! Dealer wins!")
            game_over = True
    else:
        # Dealer's turn
        dealer_total = sum(dealer_cards)
        
        # Reveal dealer's hidden card
        Blackjack.display(user_cards, dealer_cards, False)
        
        # Dealer draws cards until reaching 17 or more
        while dealer_total < 17:
            new_card = random.choice(cards)
            dealer_total, dealer_cards = Blackjack.draw_card(dealer_total, dealer_cards, new_card)
            Blackjack.display(user_cards, dealer_cards, dealer_hide=False)
            
            if dealer_total > 21:
                    print("Dealer busted! You win!")
                    game_over = True
                    break
        if not game_over:
             # Compare hands
                winner = Blackjack.check_winner(sum(user_cards), dealer_total)
                if winner == "Player":
                    print("You win!")
                elif winner == "Dealer":
                    print("Dealer wins!")
                else:
                    print("It's a tie!")
                game_over = True
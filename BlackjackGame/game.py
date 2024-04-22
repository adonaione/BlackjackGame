import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for suit in suits for rank in ranks]


random.shuffle(deck)


playerHand = [deck.pop(), deck.pop()]
dealerHand = [deck.pop(), deck.pop()]


def calculateHandValue(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank == 'Ace':
            value += 11
            aces += 1
        elif rank in ['King', 'Queen', 'Jack']:
            value += 10
        else:
            value += int(rank)
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value


while True:
    print("Player's hand:", playerHand)
    print("Dealer's hand:", dealerHand[0])
    playerValue = calculateHandValue(playerHand)
    dealerValue = calculateHandValue(dealerHand)
    if playerValue == 21:
        print("Blackjack! You win!")
        break
    elif playerValue > 21:
        print("Bust! You lose.")
        break
    else:
        action = input("Do you want to hit or stand? ")
        if action.lower() == 'hit':
            playerHand.append(deck.pop())
        elif action.lower() == 'stand':
            while dealerValue < 17:
                dealerHand.append(deck.pop())
                dealerValue = calculateHandValue(dealerHand)
            if dealerValue > 21:
                print("Dealer busts! You win!")
            elif dealerValue > playerValue:
                print("Dealer wins!")
            elif dealerValue < playerValue:
                print("You win!")
            else:
                print("Push! It's a tie.")
            break
        else:
            print("Invalid action. Please enter 'hit' or 'stand'.")
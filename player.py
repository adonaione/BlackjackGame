import random

class Player:
    hand = []
    dealer = []
    def __init__(self, isDealer):
        self.isDealer = isDealer
        self.deck = ["A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "K", "Q", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # create a function to deal 2 random cards to each player
    def deal(self):
        # identify the card to be dealt
        card = random.choice(self.deck)
        # add card to player's hand & remove from deck
        self.hand.append(card)
        self.deck.remove(card)

    # create a function that calculates the total in the players hand
    def calculate(self):
        #initiate total
        self.total = 0
        # identify face cards
        face = ['K', 'Q', 'J']
        #loop through cards in hand
        for card in self.deck:
            #add card value to total
            if card in range(1, 11):
                self.total += card
            #change face cards to number values
            elif card in face:
                self.total += 10
            # calculate Aces
            else:
                # set conditions for value = 1
                if self.total > 11:
                    self.total += 1
                # otherwise value = 11
                else:
                    self.total += 11
        return self.total
    
    # function for dealers hand
    def show_hand(self):
        # on deal, show top card only
        if len(self.dealer) == 2:
            return self.dealer[0]
        # on hits, show all cards 
        elif len(self.dealer) > 2:
            return self.dealer[0], self.dealer[1]
        
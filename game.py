from player import Player

class Game:
    
    def __init__(self):
        self.player = Player(False)
        self.dealer = Player(True)
        # self.hand = []
        # self.deal_hand = []

    def play(self):
        #game loop
        for _ in range(2):
            Player.deal(self.dealer)
            Player.deal(self.player)
        while self.player or self.dealer:
            print(f"The Dealer has: {Player.show_hand(self.dealer)} and X")
            print(f"You have: {self.player} for a total of {Player.calculate(self.player)}")
            if self.player:
                move = input("Hit/Stay: ").lower()
            # check total of dealers hand to determine hit or stay
            if Player.calculate(self.dealer) > 16:
                self.dealer = Player(False)
            # otherwise hit
            else:
                Player.deal(self.dealer)
            # on players turn, if stay, end turn with boolean
            if move == "stay":
                self.player = Player(False)
            # or deal a card
            else:
                Player.deal(self.player)
            #if busted break immediately
            if Player.calculate(self.player) >= 21: 
                break
            elif Player.calculate(self.dealer) >=21:
                break

        #if players total is 21, they win
        if Player.calculate(self.player) == 21:
            print(f"You have {self.player} for a total of 21. And the dealer has {self.dealer} for a total of {Player.calculate(self.dealer)}. You win!")
        #if dealers total 21, they win
        elif Player.calculate(self.dealer) == 21:
            print(f"You have {self.player} for a total of {Player.calculate(self.player)}. And the dealer has {self.dealer} for a total of 21. Dealer wins!")
        # if player total over 21, bust
        elif Player.calculate(self.player) > 21:
            print(f"You have {self.player} for a total of {Player.calculate(self.player)}. Bust!")
        # if dealer total over 21, they bust
        elif Player.calculate(self.dealer) > 21:
            print(f"The dealer has {self.dealer} for a total of {Player.calculate(self.dealer)}. Dealer busts!")
        # if player total higher than dealer, they win 
        elif Player.calculate(self.player) > Player.calculate(self.dealer):
            print(f"You have {self.player} for a total of {Player.calculate(self.player)}. And the dealer has {self.dealer} for a total of {Player.calculate(self.dealer)}. You win!")
        # if dealer total is greater, they win
        elif Player.calculate(self.dealer) > self.calculate(self.player):
            print(f"You have {self.player} for a total of {Player.calculate(self.player)}. And the dealer has {self.dealer} for a total of {Player.calculate(self.dealer)}. Dealer wins!")

go = Game()
go.play()
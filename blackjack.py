import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop() 
    
    def __str__(self):
        all_cards = self.deck[0].__str__()
        for i in range(1,len(self.deck)):
            all_cards += ", " + self.deck[i].__str__()
        return "Deck: " + all_cards

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet():
    while(True):
        try:
            bet = int(input("How many chips do you want to bet?: "))
            return bet
        except:
            print("Wrong input.")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}.")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Would you like to Hit or Stand (H/S)?: ")
        if x[0].upper() == 'H':
            hit(deck,hand)
            break
        elif x[0].upper() == 'S':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Wrong input.")

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Value of Dealer's Hand: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Value of Player's Hand: ", player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



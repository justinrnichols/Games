import pdb
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        self.deck_of_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.deck_of_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        
    def deal_card(self):
        return self.deck_of_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        self.player_cards = [] 
        
    def remove_card(self):
        return self.player_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards.'

def play_game(player1, player2):
    player_one = Player(player1)
    player_two = Player(player2)

    deck = Deck()
    deck.shuffle()

    for x in range(26):
        player_one.add_cards(deck.deal_card())
        player_two.add_cards(deck.deal_card())
        
    game_on = True
    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round {round_num}")

        if len(player_one.player_cards) == 0:
            print(f"Player {player1} out of cards! Game Over")
            print(f"Player {player2} Wins!")
            game_on = False
            break
        if len(player_two.player_cards) == 0:
            print(f"Player {player2} out of cards! Game Over")
            print(f"Player {player1} Wins!")
            game_on = False
            break

        player_one_cards = []
        player_one_cards.append(player_one.remove_card())
        
        player_two_cards = []
        player_two_cards.append(player_two.remove_card())
        
        at_war = True

        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print(f"Player {player1} won this round.")
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                print(f"Player {player2} won this round.")
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print('WAR!')
                if len(player_one.player_cards) < 3:
                    print(f"Player {player1} unable to play war! Game Over at War")
                    print(f"Player {player2} Wins! Player {player1} Loses!")
                    game_on = False
                    break
                elif len(player_two.player_cards) < 3:
                    print(f"Player {player2} unable to play war! Game Over at War")
                    print(f"Player {player1} Wins! Player {player2} Loses!")
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_card())
                        player_two_cards.append(player_two.remove_card())


play_game("Justin","Brennan")

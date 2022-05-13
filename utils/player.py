from msilib.schema import Icon
from multiprocessing.sharedctypes import Value
from operator import iconcat
from card import Card
from random import shuffle
from random import choices


class Player:
#player class with name , cards , turn, and history.
    def __init__(self,name): #cards,turn_count,number_of_cards,history,name
#initiate a player with the attributes
        self.cards = []
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []
        self.name = name


    
    def play(self):
        card = self.cards.pop()
        self.history.append(card)
        self.turn_count += 1
        print(f'{self.name}{self.turn_count} played:{str(card)}')
        return card

class Deck():

    def __init__(self):

        self.cards = []
        self.fill_deck()

    def fill_deck(self):
        icon = ["♥", "♦", "♣", "♠"]
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in icon:
            for v in value:
                self.cards.append(Card(i, v))
    


    def shuffle(self):
        shuffle(self.cards)


    def distribute(self, player_list):
        player_list = ["a","b","c"]



 


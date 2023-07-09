"""
Deck Class used in Blackjack_GUI.
Sets new deck of cards H,C,S,D 2-A as list.
Shuffles Deck.
Removes Cards via Stack Data Structure
Initiates player cards, player points, dealer cards, dealer points
Checks if blackjack.
Adds card to hand
"""
from Suit import Suit
from random import shuffle

class Deck():

    def __init__(self): #O(n)
        self.new_deck()
        self.shuffle()

    def new_deck(self): #O(1)
        self.deck = []
        hearts = Suit('Hearts')
        clubs = Suit('Clubs')
        spades = Suit('Spades')
        diamonds = Suit('Diamonds')
        self.deck += hearts.cards
        self.deck += clubs.cards
        self.deck += spades.cards
        self.deck += diamonds.cards

    def shuffle(self): #O(n)
        shuffle(self.deck)

    def grab_from_deck(self): #O(1)
        return self.deck.pop()
    
    def print_deck(self): #O(n)
        for card in self.deck:
            print(card)
        print(len(self.deck))

    def get_deck_count(self): #O(1)
        return len(self.deck)

    def start_round(self): #O(1)
        self.player_cards = []
        self.dealer_cards = []
        self.player_points = 0
        self.dealer_points = 0
        self.player_add_card_to_hand(self.player_cards)
        self.dealer_add_card_to_hand(self.dealer_cards)
        self.player_add_card_to_hand(self.player_cards)
        self.dealer_add_card_to_hand(self.dealer_cards)

    def dealer_add_card_to_hand(self, hand): #O(1)
        card = self.grab_from_deck()
        self.dealer_points += card.value
        hand.append(card)

    def player_add_card_to_hand(self, hand): #O(1)
        card = self.grab_from_deck()
        self.player_points += card.value
        hand.append(card)

    def check_blackjack(self, hand): #O(1)
        if hand[0].title == 'A' and hand[1].value == 10:
            return True
        elif hand[1].title == 'A' and hand[0].value == 10:
            return True
        return False
    
    def get_card_points(self, hand): #O(n)
        total = 0
        for n in hand:
            total += n.value
        return total
        
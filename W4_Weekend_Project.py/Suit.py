"""
Suit Class.
Imported in Deck.
Makes list of cards for each suit.
Adds card to list.
Sets img for each card
"""
from Card_w_notes import Card

class Suit():

    def __init__(self, name): #O(1)
        self.cards = []
        self.name = name
        self.make_suit()

    def __repr__(self):
        output = f'{self.name}:'
        for c in self.cards:
            output += f' {c.title}'
        return output
    
    def make_suit(self): #O(n)
        for num in range(2, 11):
            self.add_card(f'{num}')
        self.add_card('J')
        self.add_card('Q')
        self.add_card('K')
        self.add_card('A')

    def add_card(self, title): #O(n)
        new_card = Card(title, self.name)
        if title.isdigit():
            if 1 < int(title) < 11:
                new_card.value = int(title)
        elif title in 'KQJ':
            new_card.value = 10
        else:
            new_card.value = 1
        self.get_img(new_card, title)
        self.cards.append(new_card)
    
    def get_img(self, card, title): #O(1)
        card.img = f"W4_Weekend_Project.py/Flat_Playing_Cards_Set/{self.name}/{title}.png"
        card.back_img = "W4_Weekend_Project.py\Flat_Playing_Cards_Set\Back_Covers\Pomegranate.png"
        
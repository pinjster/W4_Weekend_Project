"""
Notes taken from HW Assignment and various rules.
Card Class imported in Suit.
Creates Card.
Can Display Card.
Assigns Title ie. 'K', value ie. 10,  suit ie. Clubs, and img and img back
"""
#Create simplified version of Blackjack using Object-Oriented Programming Techniques
#Two Players- User and Dealer(playable)
#Uses One Deck - 52 Cards (NO JOKERS) one class containing 4 deck classes / class for deck, diff class for each suit
#Four Suit classes: Diamonds, Hearts, Clubs, Spades:
#2-10: Face Value points / stored in Nodes ie. Card
#K, Q, J: 10 points
#A: 1 or 11, if A makes it equal 21, then it is 11, else 1
#At start of game, both dealer and player get two cards. / Random /
#Get higher amount of points than dealer without going over 21 / if else
#HIT: dealer gives you another card / append() / check total
#STAND: You stay then dealer takes their turn / check else append
#Dealer then plays, shows their cards.
#Dealer takes a card until reaching 17 or surpassing 21 and losing / if else
#If first deal is 21: "BLACKJACK" (player/dealer wins) / if else print
#If dealer and player num are same / ==
#BUST: for player/dealer that loses
#PUSH when both players have same amount - Tie / if ==
#Bonus-
#GAMBLE: How much money player wants to bet on round / input
#MAX BET: $1 - $1000
#when blackjack happens, bet is doubled
#SPLIT: splits the cards, doubles bet. player chooses which stack to add card to
#Only split if first deal both cards are same ie King King 
class Card():

    def __init__(self, title, suit): #O(1)
        self.title = title
        self.value = None
        self.suit = suit
        self.img = ''
        self.back_img = ''

    def __repr__(self):
        return f'{self.title} of {self.suit}'

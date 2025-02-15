#=============== part 1 ========
'''

    What is a class?
    A class is a blueprint for creating objects
    
    What is an instance?
    An instance is a specific object created from a class
    
    What is encapsulation?
    Encapsulation is the principle of restricting direct access to certain details of an object and only allowing controlled interaction through methods
    
    What is abstraction?
    Abstraction is the concept of hiding complex implementation details and exposing only what is necessary for the user
    
    What is inheritance?
    Inheritance allows a class to acquire properties and methods from another class, avoiding code duplication
    
    What is multiple inheritance?
    Multiple inheritance means a class can inherit from more than one parent class, combining their properties and behaviors
    
    What is polymorphism?
    Polymorphism allows different objects to be treated as instances of the same class through shared methods, even if they behave differently
    
    What is method resolution order or MRO?
    MRO is the order in which Python looks for methods when multiple inheritance is used
'''


#=================== part 2 =========================

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]  # newlist = [expression for item in iterable if condition == True]
        
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
        
    def shuffle_cards(self):
        random.shuffle(self.cards)
     
    def deal(self):
        if self.cards: 
            card = self.cards.pop()  
            print(f"Dealt: {card}")  
            print(f"Cards left: {len(self.cards)}")  
            return card
        else:
            print("The deck is empty.")
            return None


    

card = Deck()
card.shuffle_cards()


for _ in range(53):  #check
    card.deal()
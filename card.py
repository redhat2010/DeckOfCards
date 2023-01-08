class Card:
    
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def get_val(self):
        return self.val

    def get_suit(self):
        return self.suit

    def __str__(self):
        return str(self.val) + " of " + str(self.suit) 

# Class used to compare cards
class CardCompare:
    
    # card_val_order defines value of each type of card, in order from least to greatest
    def __init__(self,card_val_order = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King","Joker"]):
        self.card_val_order = card_val_order

    # changes the order of values for cards
    def change_card_val_order(self,new_card_val_order):
        self.card_val_order = new_card_val_order

    # compares card1 to card2 by comparing the indices 
    def compare(self,card1, card2):
        if self.card_val_order.count(card1.get_val()) == 0 or self.card_val_order.count(card2.get_val()) == 0:
            raise Exception("both card values must be in card_val_order")
        else:
            return self.card_val_order.index(card1.get_val()) - self.card_val_order.index(card2.get_val())
from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.discards = []

    # Generates the cards for the deck
    def gen_deck(self, num_decks = 1, card_vals = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King","Joker"], card_counts = [4,4,4,4,4,4,4,4,4,4,4,4,4,2], card_suits = ["hearts","spades","diamonds","clubs"]):#, suits_per_color = 2, card_colors = ["reds","blacks"]):
        
        if len(card_vals) != len(card_counts):
            raise Exception("card_vals must be same length as card_counts")
        if not isinstance(num_decks, int):
            raise Exception("num_decks must be an int")
        # if len(card_suits) != suits_per_color*len(card_colors):
        #     raise Exception("card_suits must have a length equal to suits_per_color times card_colors")
        
        card_counts = [x*num_decks for x in card_counts]

        for i in range(len(card_vals)):
            for j in range (card_counts[i]):
                self.cards.append(Card(card_vals[i],card_suits[j%len(card_suits)]))

    # removes null cards
    def remove_null(self):
        if self.cards.count(None) != 0:
            for i in range(self.cards.count(None)):
                self.cards.remove(None)
        if self.discards.count(None) != 0:
            for i in range(self.discards.count(None)):
                self.discards.remove(None)
    
    #shuffles the deck
    def shuffle(self):
        self.remove_null()
        random.shuffle(self.cards)

    # returns how many cards are left in the deck
    def cards_left(self):
        self.remove_null()
        return len(self.cards)

    # returns how many cards are left in the deck
    def cards_discarded(self):
        self.remove_null()
        return len(self.discards)

    def cards_total(self):
        self.remove_null()
        return len(self.cards) + len(self.discards)

    # draws x card from the deck
    def draw(self,x=1):
        self.remove_null()
        if x == 1:
            if self.cards_left() == 0 and self.cards_discarded() > 0:
                self.insert_cards(self.draw_discarded(self.cards_discarded()))
                self.shuffle()
            return self.cards.pop(0)
        elif x == len(self.cards):
            return_list = self.cards
            self.cards = []
            return return_list
        else:
            return_list = []
            for i in range(x):
                return_list.append(self.draw())
            return return_list

    # draws x card from the deck's discard pile
    def draw_discarded(self,x=1):
        self.remove_null()
        if (x > self.cards_discarded()):
            return None
        if x == 1:
            return self.discards.pop(0)
        elif x == len(self.discards):
            return_list = self.discards
            self.discards = []
            return return_list
        else:
            return_list = []
            for i in range(x):
                return_list.append(self.draw_discarded())
            return return_list
    
    # adds 1 or more cards to the discard pile
    def discard(self,new_cards):
        # if the new_cards are in a deck, draws all cards from that deck and inserts them
        if isinstance(new_cards,Deck):
            self.discards.extend(new_cards.draw(new_cards.cards_left()))
        # if multiple cards in a list, then insert all the cards from the list
        elif  isinstance(new_cards,list):
            self.discards.extend(new_cards)
        # otherwise, if only 1 card, just insert it
        else:
            self.discards.append(new_cards)

    # inserts 1 or more cards into the deck
    def insert_cards(self, new_cards):
        # if the new_cards are in a deck, draws all cards from that deck and inserts them
        if isinstance(new_cards,Deck):
            self.cards.extend(new_cards.draw(new_cards.cards_left()))
        # if multiple cards in a list, then insert all the cards from the list
        elif  isinstance(new_cards,list):
            self.cards.extend(new_cards)
        # otherwise, if only 1 card, just insert it
        else:
            self.cards.append(new_cards)

    #prints all cards in the deck
    def print_deck(self):
        self.remove_null()
        for i in range(len(self.cards)):
            print(self.cards[i])
    
    


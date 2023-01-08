import pygame

pygame.init()

class CardImageCreator:


    def __init__(self, vals = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King","Joker"], suits = ["hearts","spades","diamonds","clubs"]):
        self.card_base = pygame.image.load("images/card_base.png")

        self.vals = vals
        self.suits = suits

        self.card_vals = []
        self.card_suits = []

        # loads all card images for the values
        for v in vals:
            self.card_vals.append(pygame.image.load("images/card_" + str(v).lower() + ".png"))
        
        for s in suits:
            self.card_suits.append(pygame.image.load("images/card_" + str(s).lower() + ".png"))

    def create_card(self,card):
        new_card = self.card_base.copy()
        new_card.blit(self.card_suits[self.suits.index(card.get_suit())],(0,0))
        new_card.blit(self.card_vals[self.vals.index(card.get_val())],(0,0))

        return new_card
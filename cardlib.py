import random
import sys

class ExitLoop(Exception):
    pass

class card:

    def __init__(self, value, name, suit):
        self.value=value
        self.name=name
        self.suit=suit
    
    def displayName(self):
        print(f"{self.name}{self.suit}")

class hand:

    def __init__(self, playerName):
        self.cards=[]
        self.playerName=playerName
    
    def addCard(self, newCard):
        self.cards.append(newCard)
    
    def addPot(self, pot):
        for c in pot:
            self.addCard(c)
    
    def shuffleHand(self):
        random.shuffle(self.cards)
    
    def removeCardDeck(self):
        return self.cards.pop(0)
    
    def removeCardPlayer(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            print(f"{self.playerName} has run out of cards and has lost!")
            # print(f"it took {spam.count} rounds")
            raise ExitLoop
    
    def resetHand(self):
        self.cards = []
    
    def generateCards(self, cardVal, cardName, cardSuit):
        spam = card(cardVal, cardName, cardSuit)
        self.addCard(spam)

    def setupCards(self):    
        for val in range(2,15):
            if val < 11:
                for suit in ("h", "d", "s","c"):
                    self.generateCards(val, val, suit)
            else:
                match val:
                    case 11:
                        for suit in ("h", "d", "s","c"):
                            self.generateCards(val, "J", suit)
                    
                    case 12:
                        for suit in ("h", "d", "s","c"):
                            self.generateCards(val, "Q", suit)
                    
                    case 13:
                        for suit in ("h", "d", "s","c"):
                            self.generateCards(val, "K", suit)

                    case 14:
                        for suit in ("h", "d", "s","c"):
                            self.generateCards(val, "A", suit)

    def createFreshDeck(self):
        self.cards = []
        self.setupCards()

class handCounter:

    def __init__(self):
        self.count=0
    
    def incrementCount(self):
        self.count += 1
    
    def reset(self):
        self.count = 0


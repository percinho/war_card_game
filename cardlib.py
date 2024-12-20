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
    
    def returnDisplayName(self):
        return f"{self.name}{self.suit}"
    
    def reduceAce(self):
        self.value = 1
        # print(f"have reduced value to {self.value}")

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
            raise ExitLoop
    
    def resetHand(self):
        self.cards = []
    
    def generateCards(self, cardVal, cardName, cardSuit):
        spam = card(cardVal, cardName, cardSuit)
        self.addCard(spam)

    def setupCards(self, type):    
        for val in range(2,15):
            if val < 11:
                for suit in ("h", "d", "s","c"):
                    self.generateCards(val, val, suit)
            else:
                match val:
                    case 11:
                        for suit in ("h", "d", "s","c"):
                            if type == 'face':
                                val = 10
                            self.generateCards(val, "J", suit)
                    
                    case 12:
                        for suit in ("h", "d", "s","c"):
                            if type == 'face':
                                val = 10
                            self.generateCards(val, "Q", suit)
                    
                    case 13:
                        for suit in ("h", "d", "s","c"):
                            if type == 'face':
                                val = 10
                            self.generateCards(val, "K", suit)

                    case 14:
                        for suit in ("h", "d", "s","c"):
                            if type == 'face':
                                val = 11
                            self.generateCards(val, "A", suit)

    def createFreshDeck(self, type):
        self.cards = []
        self.setupCards(type)
    
    def calcHandValue(self):
        handValue = 0
        for i in self.cards:
            handValue += i.value
        return handValue
    
    def printHand(self):
        print("Your hand is: ", end="")
        for i in self.cards:
            print(i.returnDisplayName(), end=" ")
        print(f"\nThe hand value is: {self.calcHandValue()}")
    

class blackjackHand(hand):

    def __init__(self, playerName):
        super().__init__(playerName)
    
    def highAceCheck(self, card):
        if card.name == 'A' and card.value == 11:
            return True
        else:
            return False
    
    def highAceInHand(self):
        for x in self.cards:
            if x.value == 11 and x.name == 'A':
                return True
        return False
    
    def bustCheck(self):
        if self.calcHandValue() > 21 and self.highAceInHand() is True:
            for i in self.cards:
                if self.highAceCheck(i) is True:
                    i.reduceAce()
                    return None
            print(f"We shouldn't get here")
        elif self.calcHandValue() > 21:
            print(f"hand value is {self.calcHandValue()}")
            raise ExitLoop
        elif self.calcHandValue() == 21:
            print(f"hand value is {self.calcHandValue()}")
            raise ExitLoop
        else:
            return None
    
    def dealerShows(self):
        print(f"The dealer shows {self.cards[0].returnDisplayName()}")
    



class handCounter:

    def __init__(self):
        self.count=0
    
    def incrementCount(self):
        self.count += 1
    
    def reset(self):
        self.count = 0




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
            print(f"it took {spam.count} rounds")
            raise ExitLoop
    
    def resetHand(self):
        self.cards = []

class handCounter:

    def __init__(self):
        self.count=0
    
    def incrementCount(self):
        self.count += 1
    
    def reset(self):
        self.count = 0

deck = hand("deck")
p1hand = hand("Player 1")
p2hand = hand("Player 2")
spam = handCounter()

def generateCards(cardVal, cardName, cardSuit):
    spam = card(cardVal, cardName, cardSuit)
    deck.addCard(spam)

def setupCards():    
    for val in range(2,15):
        if val < 11:
            for suit in ("h", "d", "s","c"):
                generateCards(val, val, suit)
        else:
            match val:
                case 11:
                    for suit in ("h", "d", "s","c"):
                        generateCards(val, "J", suit)
                
                case 12:
                    for suit in ("h", "d", "s","c"):
                        generateCards(val, "Q", suit)
                
                case 13:
                    for suit in ("h", "d", "s","c"):
                        generateCards(val, "K", suit)

                case 14:
                    for suit in ("h", "d", "s","c"):
                        generateCards(val, "K", suit)

def dealHands():
    while len(deck.cards) > 0:
        p1hand.addCard(deck.removeCardDeck())
        p2hand.addCard(deck.removeCardDeck())
        
def playRound():
    pot =[]
    while True:
        p1card = p1hand.removeCardPlayer()
        # p1card.displayName()
        p2card = p2hand.removeCardPlayer()
        # p2card.displayName()
        pot.append(p1card)
        pot.append(p2card)
        if p1card.value > p2card.value:
            # print("p1 wins")
            p1hand.addPot(pot)
            # print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")
            # print(len(p1hand.cards))
            # print(len(p2hand.cards))
            break
        elif p2card.value > p1card.value:
            # print("p2 wins")
            p2hand.addPot(pot)
            # print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")
            # print(len(p1hand.cards))
            # print(len(p2hand.cards))
            break
        elif p1card.value == p2card.value:
            # print("It's a draw! Deal 3 and then replay!")
            for i in range(1,4):
                pot.append(p1hand.removeCardPlayer())
                pot.append(p2hand.removeCardPlayer())
            # print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")
            # print(len(p1hand.cards))
            # print(len(p2hand.cards))

def setupNewGame():
    p1hand.resetHand()
    p2hand.resetHand()
    setupCards()
    deck.shuffleHand()
    dealHands()

for x in range(1,5):
    setupNewGame()
    try:
        while True:
            playRound()
            spam.incrementCount()
    except:
        print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")
        print("Would you like to play again?")
        spam.reset()

    x+=1



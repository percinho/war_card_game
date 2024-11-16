import random
import sys
from cardlib import card, hand, handCounter, ExitLoop

deck = hand("deck")
p1hand = hand("Player 1")
p2hand = hand("Player 2")
spam = handCounter()

deck.createFreshDeck()

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
            break
        elif p2card.value > p1card.value:
            # print("p2 wins")
            p2hand.addPot(pot)
            # print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")
            break
        elif p1card.value == p2card.value:
            # print("It's a draw! Deal 3 and then replay!")
            for i in range(1,4):
                pot.append(p1hand.removeCardPlayer())
                pot.append(p2hand.removeCardPlayer())
            # print(f"p1 has {len(p1hand.cards)} and p2 has {len(p2hand.cards)} cards")

def setupNewGame():
    p1hand.resetHand()
    p2hand.resetHand()
    deck.setupCards()
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
        print(f"it took {spam.count} rounds")
        print("Would you like to play again?")
        spam.reset()

    x+=1



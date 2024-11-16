import random
import sys
from cardlib import hand, handCounter

class printStatements:

    def __init__(self):
        pass

    def stickOrTwist(self):
        print("Do you wish to (s)tick or (t)wist?")
        return input(":")
    
    def bust(self):
        print("You have gone bust")

def dealStartingHand():
    for i in range(1, 3):
        playerHand.addCard(deck.removeCardDeck())
        dealerHand.addCard(deck.removeCardDeck())

def playDealerHand():
    while dealerHand.calcHandValue() < 17:
        try:
            dealerHand.addCard(deck.removeCardDeck())
        except:
            pass

def resolveOutcome(pVal, dVal):
    if pVal > 21:
        print(f"pVal = {pVal}, dVal = {dVal}. Player busts, game over")
    elif dVal > 21:
        print(f"pVal = {pVal}, dVal = {dVal}. Dealer busts, player wins!")
    elif pVal == dVal:
        print(f"pVal = {pVal}, dVal = {dVal}. It's a Tie!")
    elif pVal > dVal:
        print(f"pVal = {pVal}, dVal = {dVal}. Player wins!")
    elif dVal > pVal:
        print(f"pVal = {pVal}, dVal = {dVal}. Dealer wins!")
    else:
        print(f"well this is awkward. pVal = {pVal}, dVal = {dVal}")
    
def gameLoop():
    dealerHand.dealerShows()
    decision = text.stickOrTwist()
    try:
        while True:
            match decision:
                case "s":
                    break
                case "t":
                    playerHand.addCard(dealerHand.removeCardDeck())
                    print(f"your card is {playerHand.cards[-1].returnDisplayName()}")
                    playerHand.bustCheck()
                    playerHand.printHand()
                    decision = text.stickOrTwist()
                case _:
                    decision = input("Please enter s or t:")
    except:
        pass

    playDealerHand()
    resolveOutcome(playerHand.calcHandValue(), dealerHand.calcHandValue())

    

text = printStatements()
deck = hand("deck")
deck.createFreshDeck('face')
deck.shuffleHand()
playerHand = hand("Player")
dealerHand = hand("Dealer")
dealStartingHand()
playerHand.printHand()
# dealerHand.printHand()

gameLoop()




print("end")



import random
import sys
from cardlib import blackjackHand, ExitLoop, bank

# Need to make sure dealer hand isn;t played out if player busts

class printStatements:

    def __init__(self):
        pass

    def stickOrTwist(self):
        print("Do you wish to (s)tick or (t)wist?")
        return input(":")
    
    def bust(self):
        print("You have gone bust")

    def betSize(self, bank):
        print(f"You have {bank}. How much do you want to bet:")

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
        print(f"Player scores {pVal}, Dealer scores {dVal}. Player busts, game over")
        return 0
    elif dVal > 21:
        print(f"Player scores {pVal}, Dealer scores {dVal}. Dealer busts, player wins!")
        return 1
    elif pVal == dVal:
        print(f"Player scores {pVal}, Dealer scores {dVal}. It's a Tie!")
        return 2
    elif pVal > dVal:
        print(f"Player scores {pVal}, Dealer scores {dVal}. Player wins!")
        return 1
    elif dVal > pVal:
        print(f"Player scores {pVal}, Dealer scores {dVal}. Dealer wins!")
        return 0
    else:
        print(f"well this is awkward. pVal = {pVal}, dVal = {dVal}")
    
def gameLoop():
    pot = playerBank.initialAnte()
    dealStartingHand()
    playerHand.printHand()
    dealerHand.dealerShows()
    decision = text.stickOrTwist()
    player_bust = 0
    while player_bust == 0:
        match decision:
            case "s":
                break
            case "t":
                playerHand.addCard(deck.removeCardDeck())
                print(f"your card is {playerHand.cards[-1].returnDisplayName()}")
                player_bust = playerHand.bustCheck()
                playerHand.printHand()
                if player_bust == 0:
                    decision = text.stickOrTwist()
                elif player_bust == 2:
                    break
                else:
                    pass
            case _:
                decision = input("Please enter s or t:")

    if player_bust == 0:
        playDealerHand()
    else:
        pass
    outcome = resolveOutcome(playerHand.calcHandValue(), dealerHand.calcHandValue())
    # print(pot)
    playerBank.resolveBet(outcome, pot)

    

playerBank = bank(50)
text = printStatements()
deck = blackjackHand("deck")
deck.createFreshDeck('face')
deck.shuffleHand()
playerHand = blackjackHand("Player")
dealerHand = blackjackHand("Dealer")



gameLoop()




print("end")



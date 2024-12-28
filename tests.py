import unittest
from cardlib import card, hand, blackjackHand, bank

testHand = blackjackHand('test_player')
Ace = card(11, 'A', 'x')
King = card(10, 'K', 'x')
Two = card(2, '2', 'x')


# The function to be tested
# def add(a, b):
#     return a + b

# The test case
class TestMathOperations(unittest.TestCase):

    def test_21(self):
        testHand.resetHand()
        testHand.addCard(Ace)
        testHand.addCard(King)
        testHand.printHand()
        # Test the add function
        self.assertEqual(testHand.bustCheck(), 2)  # This checks if add(2, 3) returns 5

        testHand.addCard(King)
        self.assertEqual(testHand.bustCheck(), 0)
        self.assertEqual(testHand.bustCheck(), 2)
    
    def test_bust(self):
        testHand.resetHand()
        testHand.addCard(King)
        testHand.addCard(King)
        testHand.addCard(Two)

        self.assertEqual(testHand.bustCheck(), 1)

if __name__ == "__main__":
    unittest.main()

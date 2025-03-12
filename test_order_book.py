import unittest
from order_book import OrderBook

class TestOrderBook(unittest.TestCase):
    def setUp(self):
        self.book = OrderBook()

    def test_trade_execution_same_price(self):
        print("Test case 1: Trade execution at same price")
        self.book.place_order(100, 5, 'bid', 'TestBot1')
        self.book.place_order(100, 5, 'ask', 'TestBot2')
        self.assertEqual(len(self.book.order_history), 1)
        print(f"Trade: {self.book.order_history[0]}")
        self.assertEqual(self.book.order_history[0], (100, 100, 5, 'TestBot1', 'TestBot2'))

    def test_partial_trade(self):
        print("Test case 2: Partial trade")
        self.book.place_order(100, 10, 'bid', 'TestBot1')
        self.book.place_order(100, 5, 'ask', 'TestBot2')
        self.assertEqual(len(self.book.order_history), 1)
        print(f"Trade: {self.book.order_history[0]}")
        self.assertEqual(self.book.bids[0][1], 5)  # 5 units left

    def test_no_trade(self):
        print("Test case 3: No trade")
        self.book.place_order(100, 5, 'bid', 'TestBot1')
        self.book.place_order(101, 5, 'ask', 'TestBot2')
        self.assertEqual(len(self.book.order_history), 0)
        print("No trade occurred")

if __name__ == '__main__':
    unittest.main()
import numpy as np
from order_book import OrderBook

class RuleBasedBot:
    def __init__(self, order_book, spread=0.5):
        self.order_book = order_book
        self.spread = spread
        self.cash = 100000
        self.inventory = 0
        self.trades = 0

    def get_mid_price(self):
        return self.order_book.mid_price() or 100

    def step(self):
        mid_price = self.get_mid_price()
        bid_price = np.round(mid_price - self.spread / 2, 2)
        ask_price = np.round(mid_price + self.spread / 2, 2)
        order_size = 5

        self.order_book.place_order(bid_price, order_size, 'bid', 'Rule Bot')
        self.order_book.place_order(ask_price, order_size, 'ask', 'Rule Bot')

        for trade in self.order_book.order_history:
            bid_price, ask_price, size, bid_bot, ask_bot = trade
            if bid_bot == 'Rule Bot':
                self.inventory += size
                self.cash -= bid_price * size
                self.trades += 1
            if ask_bot == 'Rule Bot':
                self.inventory -= size
                self.cash += ask_price * size
                self.trades += 1
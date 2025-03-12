import random
from order_book import OrderBook

class MarketMakerRL:
    def __init__(self, order_book):
        self.order_book = order_book
        self.inventory = 0
        self.cash = 100000
        self.action_space = [-1, 0, 1]
        self.spread = 0.5
        self.trades = 0
    
    def step(self):
        action = random.choice(self.action_space)
        self.spread += action * 0.1
        self.spread = max(0.3, min(0.7, self.spread))
        mid_price = self.order_book.mid_price() or 100
        bid_price = mid_price - self.spread / 2
        ask_price = mid_price + self.spread / 2
        
        self.order_book.place_order(bid_price, 5, 'bid', 'RL Bot')
        self.order_book.place_order(ask_price, 5, 'ask', 'RL Bot')
        
        for trade in self.order_book.order_history:
            bid_price, ask_price, size, bid_bot, ask_bot = trade
            if bid_bot == 'RL Bot':
                self.inventory += size
                self.cash -= bid_price * size
                self.trades += 1
            if ask_bot == 'RL Bot':
                self.inventory -= size
                self.cash += ask_price * size
                self.trades += 1
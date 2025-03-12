import time
import heapq
from collections import deque
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# Global variable for last trade price (used across components)
last_trade_price = 100.0

class Order:
    def __init__(self, order_id, price, quantity, order_type):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.order_type = order_type
        self.timestamp = time.time()

    def __repr__(self):
        return f"Order(id={self.order_id}, price={self.price}, quantity={self.quantity}, type={self.order_type})"

class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
        self.order_history = []

    def place_order(self, price, size, side, bot_name):
        if side == 'bid':
            self.bids.append((price, size, bot_name))
            self.bids.sort(reverse=True)
        else:
            self.asks.append((price, size, bot_name))
            self.asks.sort()
        self.match_orders()
    
    def match_orders(self):
        while self.bids and self.asks and self.bids[0][0] >= self.asks[0][0]:
            bid_price, bid_size, bid_bot = self.bids.pop(0)
            ask_price, ask_size, ask_bot = self.asks.pop(0)
            if bid_bot == ask_bot:
                self.bids.insert(0, (bid_price, bid_size, bid_bot))
                self.asks.insert(0, (ask_price, ask_size, ask_bot))
                break
            trade_size = min(bid_size, ask_size)
            self.order_history.append((bid_price, ask_price, trade_size, bid_bot, ask_bot))
            if bid_size > trade_size:
                self.bids.insert(0, (bid_price, bid_size - trade_size, bid_bot))
            if ask_size > trade_size:
                self.asks.insert(0, (ask_price, ask_size - trade_size, ask_bot))

    def best_bid(self):
        return self.bids[0][0] if self.bids else None

    def best_ask(self):
        return self.asks[0][0] if self.asks else None

    def mid_price(self):
        if self.bids and self.asks:
            return (self.best_bid() + self.best_ask()) / 2
        return None
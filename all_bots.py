import numpy as np
import random
from order_book import OrderBook
from rule_based_bot import RuleBasedBot
from market_maker_rl import MarketMakerRL

class RandomTrader:
    def __init__(self, order_book, name):
        self.order_book = order_book
        self.name = name
    
    def step(self):
        side = random.choice(['bid', 'ask'])
        price = (self.order_book.mid_price() or 100) + random.uniform(-1, 1)
        size = random.randint(1, 5)
        self.order_book.place_order(price, size, side, self.name)

# Simulation
order_book = OrderBook()
market_maker_rl = MarketMakerRL(order_book)
rule_based_bot = RuleBasedBot(order_book)
random_traders = [RandomTrader(order_book, f"Trader {i}") for i in range(50)]

for step in range(1001):
    for trader in random_traders:
        trader.step()
    if step % 2 == 0:
        rule_based_bot.step()
        market_maker_rl.step()
    else:
        market_maker_rl.step()
        rule_based_bot.step()
    order_book.order_history.clear()
    
    if step % 100 == 0:
        print(f"\n--- Summary after {step} steps ---")
        print(f"RL Bot PnL={market_maker_rl.cash + market_maker_rl.inventory * (order_book.mid_price() or 100) - 100000:.2f}, Trades={market_maker_rl.trades}")
        print(f"Rule Bot PnL={rule_based_bot.cash + rule_based_bot.inventory * (order_book.mid_price() or 100) - 100000:.2f}, Trades={rule_based_bot.trades}")
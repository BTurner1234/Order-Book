HFT Market-Making Bots in Python
Welcome to a mini high-frequency trading (HFT) experiment! This repo pits two market-making bots against each other in a simulated order book: a rule-based bot with fixed quotes and an RL-inspired bot that tweaks its spread. Built in Python, it’s a hands-on way to see how HFT firms profit from the bid-ask spread. Check out the article (#) for the full story!

What’s This About?
Market makers provide liquidity by quoting buy (bid) and sell (ask) prices, earning the spread when trades hit. Here, we:
Simulate an order book with 50 random traders.

Run a RuleBasedBot (fixed spread=0.5, size=5) and a MarketMakerRL (spread 0.3–0.7, size=5) for 1000 steps.

Track profit-and-loss (PnL) and trades to see who wins.

Spoiler: Timing and spread size matter—a lot!

Prerequisites
Python 3.6+

Libraries: numpy (for price rounding)

Files
order_book.py: Core order book class—stores bids/asks, matches trades, prevents self-dealing.
test_order_book.py: Unit tests for OrderBook (trade matching, partial trades, no trades).
rule_based_bot.py: RuleBasedBot with a fixed 0.5 spread, size=5, quoting around the mid-price.
market_maker_rl.py: MarketMakerRL with a dynamic spread (0.3–0.7), size=5, adjusting randomly each step.
all_bots.py: Full simulation—runs both bots with 50 random traders, alternates turns, prints PnL every 100 steps.

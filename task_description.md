# Order Book

## Background

Imagine a marketplace where people trade shares of a company (like Apple or Google).

At any given moment, there are two groups of traders:
- **Buyers**: they want to buy shares, but at the lowest price possible
- **Sellers**: they want to sell shares, but at the highest price possible

Each trader submits an **order** saying: "I want to buy/sell X shares at $Y per share."
These orders don't execute immediately, they go into a queue called the **order book**, where they wait until someone on the other side is willing to trade at a compatible price.

The order book is the core data structure that sits at the heart of every stock exchange and trading platform. Its job is simple: collect orders from
buyers and sellers, and whenever a buyer's price meets or exceeds a seller's price, execute a trade between them.

### Key terms

- **Buy order (bid)**: "I want to buy 100 shares, and I'm willing to pay up to $10.50 each"
- **Sell order (ask)**: "I want to sell 50 shares, and I won't accept less than $10.25 each"
- **Matching**: When the highest buy price >= the lowest sell price, a trade happens automatically
- **Trade**: The actual exchange. Shares move from seller to buyer, money moves from buyer to seller

## Task 1: The Book (no matching)

Build the book itself. Just storing and organizing orders. No trading happens yet.

**Implement:**
- `add_order(side, price, quantity)`: Add an order to the correct side
- `get_bids()`: Return buy orders sorted highest price first
- `get_asks()`: Return sell orders sorted lowest price first

**Rules:**
- Buy orders sorted **highest price first** (best bid on top)
- Sell orders sorted **lowest price first** (best ask on top)

**Example:**
```python
book.add_order("buy", 10.00, 100)
book.add_order("buy", 10.50, 50)
book.add_order("sell", 11.00, 80)
book.add_order("sell", 10.75, 30)

book.get_bids()  # [{"price": 10.50, "quantity": 50}, {"price": 10.00, "quantity": 100}]
book.get_asks()  # [{"price": 10.75, "quantity": 30}, {"price": 11.00, "quantity": 80}]
```

## Testing

A basic test file `test_order_book.py` is provided with one starter test per round.

You should extend it with more test cases.

Think about:
- Edge cases (zero? negative? what can go wrong?)
- Multiple orders at the same price etc

Run your tests with:
```bash
python3 -m pytest test_order_book.py
```

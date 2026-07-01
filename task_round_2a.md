## Round 2a: Exact Match

Now make the book actually trade! Start simple: when a new order arrives, check
if it can match against the **best** order on the other side, and both have the
same quantity.

**Implement:**
- Matching logic inside `add_order`: just one match
- `get_trades()`: Return list of executed trades

**Rules:**
- A match happens when: `best bid price >= best ask price`
- The trade executes at the **resting** order's price (the order already in the book)
- For now, all orders have the same quantity, so ignore order size for now

**Example:**
```python
book.add_order("buy", 10.50, 100)   # No asks yet, sits in book
book.add_order("sell", 10.25, 100)  # Best bid 10.50 >= 10.25, MATCH!

# Trade: 100 shares @ $10.50 (resting order's price)
# Both orders fully filled and removed

book.get_trades()  # [{"price": 10.50, "quantity": 100}]
book.get_bids()    # []
book.get_asks()    # []
```

**Hints:**
- When a sell comes in, check if there are any bids and if the best bid's price >= the sell price
- When a buy comes in, check if there are any asks and if the buy price >= the best ask's price
- If they match, create a trade dict `{"price": ..., "quantity": ...}` and store it in a trades list
- Remove both orders from the book after the trade

---

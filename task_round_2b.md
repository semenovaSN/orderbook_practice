## Task 2b: Partial Fills

What if the two orders have **different** quantities? The smaller one fills
completely, and the leftover stays in the book.

**Implement:**
- Update your matching logic to handle unequal quantities

**Rules:**
- Trade quantity = `min(incoming quantity, resting quantity)`
- If the resting order has leftover quantity, update it (don't remove it)
- If the incoming order has leftover quantity, add the remainder to the book

**Example:**
```python
book.add_order("buy", 10.50, 50)    # Sits in book
book.add_order("sell", 10.25, 30)   # Best bid 10.50 >= 10.25, MATCH!

# Trade: 30 shares @ $10.50 (resting order's price)
# Buy had 50 shares, 30 matched, 20 remain in the book

book.get_trades()  # [{"price": 10.50, "quantity": 30}]
book.get_bids()    # [{"price": 10.50, "quantity": 20}]
book.get_asks()    # []
```

**Hints:**
- Use `min(remaining, resting["quantity"])` to find the trade quantity
- Subtract the trade quantity from both orders
- Remove an order only when its quantity hits 0

---

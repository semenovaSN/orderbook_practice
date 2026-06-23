"""
Tests for the Order Book.
Run with: python3 -m pytest test_order_book.py

TODO: Add more test cases for each round
"""

from order_book import OrderBook


# --- Round 1: Adding and sorting ---

def test_add_single_buy():
    book = OrderBook()
  
    book.add_order("buy", 10.00, 100)
    bids = book.get_bids()
  
    assert len(bids) == 1
    assert bids[0]["price"] == 10.00
    assert bids[0]["quantity"] == 100

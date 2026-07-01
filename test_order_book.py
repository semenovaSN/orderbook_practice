"""
Tests for the Order Book.
Run with: python3 -m pytest test_order_book.py

TODO: Add more test cases for each round
"""

from order_book import OrderBook
import pytest

# --- Round 1: Adding and sorting ---

def test_add_single_buy():
    book = OrderBook()

    book.add_order("buy", 10.00, 100)
    bids = book.get_bids()

    assert len(bids) == 1
    assert bids[0]["price"] == 10.00
    assert bids[0]["quantity"] == 100

def test_same_price():
    book = OrderBook()

    book.add_order("buy", 12.00, 100)
    book.add_order("buy", 12.00, 70)
    bids = book.get_bids()

    assert len(bids) == 2

    assert bids[0]["price"] == 12.00
    assert bids[0]["quantity"] == 100

    assert bids[1]["price"] == 12.00
    assert bids[1]["quantity"] == 70

def test_invalid_values():
    book = OrderBook()

    with pytest.raises(ValueError, match="Invalid value"):
        book.add_order("buy", -12.00, 50)
    with pytest.raises(ValueError, match="Invalid value"):
        book.add_order("buy", 0.0, 40)
    with pytest.raises(ValueError, match="Invalid value"):
        book.add_order("sell", 10.0, -40)

    bids = book.get_bids()
    assert len(bids) == 0

def test_invalid_input():
    book = OrderBook()

    with pytest.raises(ValueError, match="Invalid input"):
        book.add_order(4, "sell", 10.0)
    with pytest.raises(ValueError, match="Invalid input"):
        book.add_order(25, True, "aaa")
    with pytest.raises(ValueError, match="Invalid input"):
        book.add_order("selll", 25.0, 10)

    bids = book.get_bids()
    assert len(bids) == 0
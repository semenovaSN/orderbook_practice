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

def test_right_order_buys():
    book = OrderBook()

    book.add_order("buy", 12.00, 70)
    book.add_order("buy", 14.00, 70)
    book.add_order("buy", 8.00, 70)
    book.add_order("buy", 10.00, 70)
    bids = book.get_bids()

    assert len(bids) == 4

    assert bids[0]["price"] == 8.00
    assert bids[0]["quantity"] == 70

    assert bids[1]["price"] == 10.00
    assert bids[1]["quantity"] == 70

    assert bids[2]["price"] == 12.00
    assert bids[2]["quantity"] == 70

    assert bids[3]["price"] == 14.00
    assert bids[3]["quantity"] == 70


def test_right_order_sells():
    book = OrderBook()

    book.add_order("sell", 12.00, 70)
    book.add_order("sell", 14.00, 70)
    book.add_order("sell", 8.00, 70)
    book.add_order("sell", 10.00, 70)
    asks = book.get_asks()

    assert len(asks) == 4

    assert asks[0]["price"] == 14.00
    assert asks[0]["quantity"] == 70

    assert asks[1]["price"] == 12.00
    assert asks[1]["quantity"] == 70

    assert asks[2]["price"] == 10.00
    assert asks[2]["quantity"] == 70

    assert asks[3]["price"] == 8.00
    assert asks[3]["quantity"] == 70

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

def test_valid_trade():
    book = OrderBook()

    book.add_order("buy", 14.00, 70)
    book.add_order("sell", 12.00, 70)

    book.add_order("sell", 12.00, 70)
    book.add_order("buy", 18.00, 70)

    book.add_order("sell", 12.00, 70)
    book.add_order("sell", 8.00, 70)
    book.add_order("buy", 18.00, 70)
    trades = book.get_trades()
    asks = book.get_asks()

    assert len(trades) == 3
    assert len(asks) == 1

    assert trades[0]["price"] == 14.00
    assert trades[0]["quantity"] == 70

    assert trades[1]["price"] == 12.00
    assert trades[1]["quantity"] == 70

    assert trades[2]["price"] == 8.00
    assert trades[2]["quantity"] == 70
"""
Order Book

Read task_description.md for full details.
"""

from typing import TypedDict


class Order(TypedDict):
    price: float
    quantity: int


class OrderBook:
    def __init__(self) -> None:
        # TODO: Initialize your data structures
        pass

    # Round 1: Add orders and return them sorted

    def add_order(self, side: str, price: float, quantity: int) -> None:
        """
        Add an order to the book.
        """
        # TODO Round 1: Add to the correct list and keep it sorted
        pass

    def get_bids(self) -> list[Order]:
        """Return current buy orders, sorted highest price first."""
        # TODO
        return []

    def get_asks(self) -> list[Order]:
        """Return current sell orders, sorted lowest price first."""
        # TODO
        return []


# You can use this to test manually while developing
if __name__ == "__main__":
    book = OrderBook()

    book.add_order("buy", 10.00, 100)
    book.add_order("buy", 10.50, 50)
    book.add_order("sell", 11.00, 80)

    print("Bids:", book.get_bids())
    print("Asks:", book.get_asks())

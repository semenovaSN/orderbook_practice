"""
Order Book

Read task_description.md for full details.
"""

from typing import TypedDict

bids = []
asks = []

class Order(TypedDict):
    price: float
    quantity: int


class OrderBook:

    def __init__(self, side=None, price=0.0, quantity=0) -> None:
        # TODO: Initialize your data structures
        self.side = side
        self.price = price
        self.quantity = quantity
        pass

    # Round 1: Add orders and return them sorted

    def add_order(self, side: str, price: float, quantity: int) -> None:
        """
        Add an order to the book.
        """
        # TODO Round 1: Add to the correct list and keep it sorted
        if side not in ["buy", "sell"] or type(price) != float or type(quantity) != int:
            raise ValueError("Invalid input")
        elif price <= 0.0 or quantity <= 0:
            raise ValueError("Invalid value")

        if side == "buy":
            bids.append({"price": price, "quantity": quantity})

            if len(bids) > 1:
                sorted_list = sorted(bids, key=lambda d: d['price'], reverse=True)
                #print("sort true:", sorted_list)

                return sorted_list


        elif side == "sell":
            asks.append({"price": price, "quantity": quantity})

            if len(asks) > 1:
                sorted_list = sorted(asks, key=lambda d: d['price'])
                #print("sort true:", sorted_list)

                return sorted_list

    def get_bids(self) -> list[Order]:
        """Return current buy orders, sorted highest price first."""
        # TODO
        global bids
        temp = bids
        bids = []
        return temp

    def get_asks(self) -> list[Order]:
        """Return current sell orders, sorted lowest price first."""
        # TODO
        global asks
        temp = asks
        asks = []
        return temp


# You can use this to test manually while developing
if __name__ == "__main__":
    book = OrderBook()

    book.add_order("buy", 10.00, 100)
    book.add_order("buy", 11.50, 50)
    book.add_order("sell", 11.00, 80)
    book.add_order("sell", 10.75, 30)

    print("Bids:", book.get_bids())
    print("Asks:", book.get_asks())
    bids = []
    asks = []

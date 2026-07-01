"""
Order Book

Read task_description.md for full details.
"""

from typing import TypedDict, Any


class Order(TypedDict):
    price: float
    quantity: int


class OrderBook:

    def __init__(self, side=None, price=0.0, quantity=0) -> None:
        # TODO: Initialize your data structures
        self.bids = []
        self.asks = []
        self.trades = []
        pass

    # Round 1: Add orders and return them sorted

    def add_order(self, side: str, price: float, quantity: int) -> Any:
        """
        Add an order to the book.
        """
        # TODO Round 1: Add to the correct list and keep it sorted
        def trade(self, price, quantity) -> None:
            self.trades.append({"price": price, "quantity": quantity})

        if side not in ["buy", "sell"] or type(price) != float or type(quantity) != int:
            raise ValueError("Invalid input")
        elif price <= 0.0 or quantity <= 0:
            raise ValueError("Invalid value")

        if side == "buy":
            self.bids.append({"price": price, "quantity": quantity})
            self.bids = sorted(self.bids, key=lambda d: d['price'], reverse=True)
            self.asks = sorted(self.asks, key=lambda d: d['price'])

            for i in self.asks:
                if i["price"] <= price:
                    trade(self, i["price"], i["quantity"])
                    self.asks.remove(i)
                    self.bids.remove({"price": price, "quantity": quantity})
                    self.bids = sorted(self.bids, key=lambda d: d['price'])
                    self.asks = sorted(self.asks, key=lambda d: d['price'], reverse=True)
                    break

            self.bids = sorted(self.bids, key=lambda d: d['price'])
                #print("sort true:", sorted_list)

            return self.bids

        elif side == "sell":
            self.asks.append({"price": price, "quantity": quantity})

            self.bids = sorted(self.bids, key=lambda d: d['price'], reverse=True)
            self.asks = sorted(self.asks, key=lambda d: d['price'])

            for i in self.bids:
                if i["price"] >= price:
                    trade(self, i["price"], i["quantity"])
                    self.bids.remove(i)
                    self.asks.remove({"price": price, "quantity": quantity})
                    self.bids = sorted(self.bids, key=lambda d: d['price'])
                    self.asks = sorted(self.asks, key=lambda d: d['price'], reverse=True)
                    break


            self.asks = sorted(self.asks, key=lambda d: d['price'], reverse=True)
                #print("sort true:", sorted_list)

            return self.asks


    def get_trades(self):
        return self.trades

    def get_bids(self) -> list[Order]:
        """Return current buy orders, sorted highest price first."""
        # TODO
        self.bids = sorted(self.bids, key=lambda d: d['price'])
        return self.bids

    def get_asks(self) -> list[Order]:
        """Return current sell orders, sorted lowest price first."""
        # TODO
        self.asks = sorted(self.asks, key=lambda d: d['price'], reverse=True)
        return self.asks


# You can use this to test manually while developing
if __name__ == "__main__":
    book = OrderBook()

    book.add_order("sell", 10.0, 100)
    book.add_order("sell", 5.0, 100)
    book.add_order("sell", 100.0, 100)
    book.add_order("buy", 1000.0, 100)

    print("Bids:", book.get_bids())
    print("Asks:", book.get_asks())
    print("Trades:", book.get_trades())
# Define your exception up here:
class OutOfStock(Exception):
    "This item is out of stock."

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] == 0:
        raise OutOfStock
    else:  
        self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
# candle_shop.buy('blue')
try:
    print(candle_shop.stock)
    print(candle_shop.buy('green'))
    print(candle_shop.stock)
except OutOfStock:
    print("this")

# This should raise OutOfStock:
# candle_shop.buy('green')

    
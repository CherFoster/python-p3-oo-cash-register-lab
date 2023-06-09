#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.prices = []
    self.last_transaction_total = 0

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title]* quantity)
    self.prices.extend([price] * quantity)
    self.last_transaction_total = price * quantity

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.total * self.discount / 100
      self.total = int(self.total)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if len(self.items) == 0:
      self.total = 0.0
      self.last_transaction_total = 0
    else:
      self.total -= self.last_transaction_total
      self.prices.pop()
      self.items.pop()
      self.last_transaction_total = 0




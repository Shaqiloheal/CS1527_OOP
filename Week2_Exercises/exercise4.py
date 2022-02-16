# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 4
# Program that defines a Counter class.

class Counter:
    """Defines Counter class"""

    inc_total = 0   # class attributes
    count_total = 0

    def __init__(self):
        self._my_total = 0   # data attribute
        Counter.count_total += 1

    def reset(self):
        """Resets the total count"""
        self._my_total = 0

    def increment(self, amount = 1):
        """Increments the count"""
        Counter.inc_total += 1
        self._my_total += amount

    def decrement(self, amount = 1):
        self._my_total -= amount
        

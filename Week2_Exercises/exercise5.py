# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 5
# Defines a custom class which is inherited from the
# built in class Exception.

class CustomError(Exception):
    """Custom exception class"""

    def __init__(self, message):
        self.message = message
        
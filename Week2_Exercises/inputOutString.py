# Author: Warren Spalding
# CS1527 - Object Orientated Programming
# Week 2 - Exercise 2
# Defines a class InputOutString

class InputOutString:

    """"""
    def __init__(self):
        self._word = ""
        
    def get_string(self):
        self._word = input("Please enter a word: " )
        

    def print_string(self):
        print("Your word in upper case is: " + self._word.upper())

word_1 = InputOutString()
word_1.get_string()
word_1.print_string()







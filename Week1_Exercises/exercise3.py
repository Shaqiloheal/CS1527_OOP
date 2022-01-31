# Author: Warren Spalding
# Date: 31 January 2022
# Python Warm-Up & Recap
# Exercise 3

currentYear = int(input("Please enter a 4 digit year: "))

num1 = currentYear % 400
num2 = num1 % 100
num3 = num2 % 4

if num1 == 0:
    lYear = 'a'
elif num2 == 0:
    lYear = 'not a'
elif num3 == 0:
    lYear = 'a'
else:
    lYear = 'not a'

print("The year that has been entered is", lYear, "leap year.")
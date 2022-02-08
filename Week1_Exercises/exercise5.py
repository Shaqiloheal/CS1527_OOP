# Author: Warren Spalding
# Date: 2 Feburary 2022
# Python Warm-Up & Recap
# Exercise 5
# function which returns reverse of a string
def isPalindrome(userInput):
    return userInput == userInput[::-1]

# user's input
userInput = str(input("Please enter any word: "))
answer = isPalindrome(userInput)

if answer:
    print(userInput,"is a palindrome.")
else:
    print(userInput,"is not a palindrome.")



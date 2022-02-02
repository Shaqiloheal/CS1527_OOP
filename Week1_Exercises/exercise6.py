# Author: Warren Spalding
# Date: 2 Feburary 2022
# Python Warm-Up & Recap
# Exercise 6

# user input
num = int(input("Please enter a number: "))

# define flag variable
flag = False

# prime numbers that are greater than 1
if num > 1:
    # check factors
    for i in range(2, num):
        if (num % i) == 0:
             # if the factor is found, sets the flag to True
             flag = True
        break

# check if flag is True
if flag:
    print(num, "is not a prime number.")
else:
    print(num, "is a prime number.")

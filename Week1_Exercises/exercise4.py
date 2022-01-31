# Author: Warren Spalding
# Date: 31 January 2022
# Python Warm-Up & Recap
# Exercise 4

celcius = 0

print("  def.F  deg.C")

while celcius <= 100:
    fahrenheit = celcius * (9/5) + 32
    print('%6.0f %8.0f' % (fahrenheit, celcius)) #This line positions the table.
    celcius += 10


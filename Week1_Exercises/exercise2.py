# Author: Warren Spalding
# Date: 31 January 2022
# Python Warm-Up & Recap
# Exercise 2

currentYear = int(input("Please input a four digit year: "))

if (currentYear - 2000) % 12 == 0:
    zodiac = 'Dragon'
elif (currentYear - 2000) % 12 == 1:
    zodiac = 'Snake'
elif (currentYear - 2000) % 12 == 2:
    zodiac = 'Horse'
elif (currentYear - 2000) % 12 == 3:
    zodiac = 'Sheep'
elif (currentYear - 2000) % 12 == 4:
    zodiac = 'Monkey'
elif (currentYear - 2000) % 12 == 5:
    zodiac = 'Rooster'
elif (currentYear - 2000) % 12 == 6:
    zodiac = 'Dog'
elif (currentYear - 2000) % 12 == 7:
    zodiac = 'Pig'
elif (currentYear - 2000) % 12 == 8:
    zodiac = 'Rat'
elif (currentYear - 2000) % 12 == 9:
    zodiac = 'Ox'
elif (currentYear - 2000) % 12 == 10:
    zodiac = 'Tiger'
else:
    zodiac = 'Hare'

print("The current Chinese Zodiac animal is the", zodiac)
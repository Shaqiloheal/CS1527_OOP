# Author: Warren Spalding
# Date: 2 Feburary 2022
# Python Warm-Up & Recap
# Exercise 7

# function that verifys password strength
def pass_check(passWord):
    # check length of password
    len_error = len(password) < 8
    # search for digits
    dig_error = re.search(r"\d", passWord) is None
    # search for upper case
    uppercase_error = re.search(r"[A-Z]", passWord) is None
    # search for lower case
    lowercase_error = re.search(r"[a-z]", passWord) is None
    # password result
    passWord_good = not (len_error or dig_error or uppercase_error or lowercase_error)
return{'passWord_good' : passWord_good}


passWord = input("Please input a password of your choice: ")


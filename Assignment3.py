
## Assignment 3
##
## Austin Thiel
## Professor Gumm CPSC230-03
## 19 September 2013
##
## "This is insane"
##

import random


## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ##
print "## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ## TASK 1 ##"
print

def snark():
    randomPick = random.randint(1,5) # picks a number in the range 1,..., 5
    # based on the random pick, form a comment and return it.
    if randomPick == 1:
        result = "Hmm"
    elif randomPick == 2:
        result = "Well now."
    elif randomPick == 3:
        result = "OK."
    elif randomPick == 4:
        result = "Yikes. Wasn't expecting that!"
    else:
        result = "My, aren't you clever."
    return result

high = 1001
low = 1

secret_num = input("Please enter a whole number from 0-1000 : ")

guess = (high-low)/2
while guess != secret_num:
    ask_bigger = raw_input("Is your number bigger than " + str(guess) + "? (yes/no): ")
    if ask_bigger == "yes":
        low = guess
    elif ask_bigger == "no":
        high = guess
    guess = (high+low)/2
    print snark()
    print
    ask_smaller = raw_input("Is your number less than " + str(guess) + "? (yes/no): ")
    if ask_smaller == "yes":
        high = guess
    elif ask_smaller == "no":
        low = guess
    guess = (high+low)/2
    print snark()
    print
print "Oh. Oh. Oh. I got it! Your number is",guess

print

## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ##
print "## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ## TASK 2 ##"
print

def decToBin(n):
    if n == 0:
        return ''
    else:
        n = decToBin(n/2) + str(n%2)
        return n
    
user_input = input("Please enter a decimal numeral to be converted to binary : ")
print decToBin(user_input)

print

def decToHex(n):
    x = (n % 16)
    digits = "0123456789ABCDEF"
    rest = n / 16
    if rest == 0:
        return digits[x]
    return decToHex(rest) + digits[x]

user_input = input("Please enter a decimal numeral to be converted to hexadecimal : ")
print decToHex(user_input)

print

## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ##
print "## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ## TASK 3 ##"
print

def daysInYear(year):
    if year%400 == 0 or year%4 == 0 and year%100 != 0:
        year = 366
    else:
        year = 365
    return year

user_input_1 = input("Enter a year to find out how many days it contains : ")
print daysInYear(user_input_1)

print

def daysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        month = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        month = 30
    elif month == 2 and daysInYear(user_input_3) != 366:
        month = 28
    else:
        month = 29
    return month

user_input_2 = input("First, enter a month : ")
user_input_3 = input("Next, enter a year to find out how many days the month contains : ")
print daysInMonth(user_input_2, user_input_3)

print

def isValidDate(day, month, year):
    if user_input_4 <= daysInMonth(user_input_5, user_input_6) and user_input_4 != 0:
        return True
    else:
        return False

print "This will check if the inputted date is valid"
print
user_input_4 = input("Enter a day : ")
user_input_5 = input("Enter a month : ")
user_input_6 = input("Enter a year : ")

print isValidDate(user_input_4,user_input_5,user_input_6)

print

def monthSinceMarch(month):
    if month >= 3 and month <= 12:
        month = month - 3
    elif month == 2:
        month = 11
    elif month == 1:
        month = 10
    total = 0
    i = month
    days = 0

    while i > 0:
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            month = 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            month = 30
        elif i == 2:
            month = 28
        total = total + month
        i-=1
    return total + 3
    
def daysSince1March(day):
    daysInMonth = day - 1
    return daysInMonth

print "This will tell you how many days away your date is from the previous March 1st"

print

user_input_7 = input("Enter a day : ")
user_input_8 = input("Enter a month : ")

print daysSince1March(user_input_7) + monthSinceMarch(user_input_8)

print
print

## I love CompSci
    
    



        
    








#
# Assignment 2
#
# Austin Thiel
# CPSC230-03 Gumm
# 10 September 2013
#
#"not too bad"

#
# Task 1
#

total = 0
n = 0

print "###################################################"
print "TASK 1"
print "###################################################"
print

print "Please keep entering integers, type a dot '.' when finished."
print
while True:
    n = raw_input("Next number, please : ")
    if n.isdigit():
        total += int(n)
    elif n == '.':
        print "The total is :",total
        break
    else:
        print "I will ignore this input"
print

#
# Task 2 
#

print "###################################################"
print "TASK 2"
print "###################################################"
print

A = int(input("Please enter the first number you would like to multiply : "))
B = int(input("Please enter the second number you would like to multiply : "))
total = 0
while B != 0:
    if B%2 != 0:
        total += A
        A*=2
        B/=2
    if B%2 == 0:
        A*=2
        B/=2
print "The product is", total
print
        
#
# Task 3
#

print "###################################################"
print "TASK 3"
print "###################################################"
print

userString = raw_input("Please enter any text : ")
for vowel in 'aeiouAEIOU':
    userString = userString.replace(vowel,'')
print userString



    
    
    


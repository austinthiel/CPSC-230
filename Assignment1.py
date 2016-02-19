#
#Preliminary Assignment - Playing with Python
#
#Austin Thiel
#CPSC230-03
#Professor H. Peter Gumm
#8/29/2013
#
#UPDATED on 10/1/2014



for i in range(5):
    line = ""
    for j in range(7):
        line+='*'
    print line
    
print

line = "*" 
for i in range(5):
    print line
    line+='*'

print

for i in range(10):
    line = ""
    if i%2 == 0:
        d = ' '
    else:
        line += d
    for j in range(10):
        if j%2 == 0:
            c = ' '
        else:
            c = '*'
        line += c
    print line

print

s = "OXOXOXOX"
for i in range(8):
    print s
    s = s[1:]

print

s = "   X"
for i in range(4):
    print s
    s=s[1:]
    s+="XX"

print

s = "     |     |"
t = "-----+-----+-----"
for i in range(5):
    if i%2 == 0:
        print s
    else:
        print t

print

        
        
    
        
        

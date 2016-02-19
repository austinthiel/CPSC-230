# README # README # README # README # README # README # README # README # README #  
# README # README # README # README # README # README # README # README # README #

# I was given an extension for this assignment by Dr. Gumm
# and emailed it to him when I was finished,
# but I forgot to upload it to moodle
# if there is any confusion, please email me
# thiel105@mail.chapman.edu

# README # README # README # README # README # README # README # README # README #
# README # README # README # README # README # README # README # README # README #


#TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1 #TASK 1

def howManyAtoms(atom):
    for i in range(len(atom)):
        if atom[i].isdigit():
            car = atom[:i]
            carend = atom[i:]
        else:
            car = i
            carend = i
    ls = []
    for i in range(int(carend)):
        ls.append(car)
    return ls


def feasible2(right, left):
    ls = []
    for i in right:
        for z in range(i[0]):            
            ls.append(i[1])
    newls = []
    for i in ls:
        newls += (splitAtoms(i))   
    dic = {}
    for i in newls:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1       
    ls1 = []
    for i in left:
        for z in range(i[0]):            
            ls1.append(i[1])
    newls2 = []
    for i in ls1:
        newls2 += (splitAtoms(i))   
    dic2 = {}
    for i in newls2:
        if i in dic2:
            dic2[i] += 1
        else:
            dic2[i] = 1
    if dic == dic2:
        return True
    else:
        return False

    
def feasible(x,y):
    splitR = splitReaction(x)
    splitY = splitReaction(y)
    ls = []
    for i in range(len(splitR)):
        quantMo = splitOffNumbaPrefix(splitR[i])
        ls.append(quantMo)
    print ls
    ls1 = []
    for i in range(len(splitY)):
        quantMo1 = splitOffNumbaPrefix(splitY[i])
        ls1.append(quantMo1)

    print feasible2(ls, ls1)

    
def splitReaction(x):
    car = [s.strip() for s in x.split("+")]
    return car      
    

def splitOffNumbaPrefix(x):
    i = 0
    for c in range(len(x)):
        if not x[c].isdigit():
            break
        i += 1
    if i == 0:
        return 1, x
    else:
        return int(x[:i]), x[i:]
    
   
def splitAtoms(s):
    starts = [i for i in range(len(s)) if s[i].isupper()] + [len(s)]
    car = [s[starts[k]:starts[k+1]] for k in range(len(starts)-1)]
    print car
    ls = []
    cow = []
    for i in car:
        if len(i) > 1:
            cow += howManyAtoms(i)
            
        else:
            ls.append(i)
    return cow + ls


    
#TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 #TASK 2 



def splitpoly(pstr): #breaks up the polynomial at "+,-"       
    y = '+'
    polystr = pstr.replace('-','+-')
    return [s for s in polystr.split('+')]


def readPoly(): #have the user enter in the polynomial then split it up
    cow = input('Enter coefficients in string form, separate using + or -:')
    cow = splitpoly(cow) #run input thru split function
    if cow[0] == '':
        cow.remove('') #remove extra spaces
    return cow


def polynomial(x): #use the coefficients to create the function
    polynomial = ''
    for i in range(len(x)):
        if not x[i].isdigit(): #if it is a digit break
            continue
        if not int(x[i]) == 0:
            if x[i].isdigit() and x[i]>0 and polynomial != '':
                polynomial += '+ '
            if i == 0:
                polynomial += x[i]
            elif x[i] == 1:
                polynomial += str('x**'+str(i))
            else:                
                polynomial += str(str(x[i])+'*x**'+str(i))
            if i != 0 or i+1 != len(x) :
                polynomial += ' '
    return polynomial


def polySum(x,y): #ADD TWO POLYNOMIALS
    polySum = []
    if x > y:
        z = y
    else:
        z = x
    for i in range(len(z)):
        polySum += [int(y[i]) + int(x[i])] #add the coefficients together
    return polySum


def maxPower(car): # Greatest power
    pwr = 0
    for i in car:
        if i[-1].isdigit() and i[-1] > pwr and len(i)>3: #find the highest power
            pwr = i[-1]
        else:
            pwr = 1
    return int(pwr)

            
def polyMult(x,y): #multiply the polynomials
    polynomial = []
    if x > y:
        a = x
        b = y
    else:
        a = y
        b = x
    for i in range(len(a)):
        if i == 0:
            polynomial += [int(a[i]) *int(b[i])]
            continue
        if i == 1:
            polynomial += [int(a[i]) * int(b[i-1])+int(a[i-1])*int(b[i])]
        else:
            cow = 0
            for j in range(len(a)):
                if i < len(b):
                    cow += int(b[i])*int(a[j])
                if i == 0:
                    break
                i -= 1
            polynomial += [cow]
    return polynomial


def derivative(x): #use the power rule to take the derivative
    polynomial = ''
    for i in range(len(x)):
        if i == 0:
            polynomial = polynomial
        elif int(x[i]) == 0:
            polynomial += '+'
        elif i == 1:
            polynomial += str(int(x[i]))
        else:
            polynomial += str(int(x[i])*i)+'x'+'**'+str((i-1))
        if i+1 != len(x)and i > 0 and int(x[i+1])> 0 and int(x[i])!=0:
            polynomial += '+'            
    return polynomial


def buildPoly(): #recalls all functions to build that polynomial you always wanted
    polynomial = readPoly()
    print polynomial
    polynomial1 = readPoly()
    print polynomial1
    a = polynomial(polynomial)
    b = polynomial(polynomial1)
    c = polySum(polynomial,polynomial1)
    d = polyMult(polynomial,polynomial1)
    e = deriv(polynomial)
    f = deriv(polynomial1)
    return a,b,c,d,e,f

#TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 #TASK 3 

import urllib
mobydickUrl = urllib.urlopen('http://introcs.cs.princeton.edu/java/data/mobydick.txt')
tomsawyerUrl = urllib.urlopen('http://introcs.cs.princeton.edu/java/data/TomSawyer.txt')
ihatethisbookUrl = urllib.urlopen('http://introcs.cs.princeton.edu/java/data/tale.txt')


def index(txt):
    newset = set([]) #create a new set
    cnt = 1
    for line in txt:
        if cnt >= 1000: #check lines greater than 999
            return newset
        ls1 = line.strip('\r\n').lower().translate(None, '-,.!:;"?/@%&').split(' ') #Formats text to be processed by separating the text at each line, lowering case, ignoring symbols, and splitting at the spaces
        if len(ls1) > 1: #First reads lines that are longer that one word
            for i in ls1:
                if len(i) > 6: #Checks only words longer than 6 letters
                    newset.add(i)
            cnt += 1
    return newset


def onlymelville(mobydick,tomsawyer,ihatethisbook): #find the words only in moby dick
    dfrence1 = mobydick.difference(ihatethisbook)
    dfrence2 = mobydick.difference(tomsawyer)
    return dfrence1.union(dfrence2) 


def notMelville(mobydick,tomsawyer,ihatethisbook): #find the words not in moby dick
    smewd = mobydick.union(tomsawyer)
    smeTom = smewd.difference(mobydick)
    smewd = mobydick.union(ihatethisbook)
    smeIHTB = smewd.difference(mobydick)
    smeResult = smeTom.union(smeIHTB)
    return smeResult


def sets(): 
    mele = index(mobydickUrl)
    twai = index(tomsawyerUrl)
    dics = index(ihatethisbookUrl)
    print "Words longer than 6 characters found only in Moby Dick: \n"
    print onlymelville(mele,twai,dics)
    print "\nMoby Dick's longest word: " + max(mele, key=len)
    print "Tale of Two Cities's longest word: " + max(dics, key=len)
    print "Tom Sawyer's longest word: " + max(twai,key=len)
    print "\nWords used by Dickens and Twain, but not by Melville: \n"
    print notMelville(mele,twai,dics)
    

# TASK 1

# SUBTASK A & B

def minSort(ls):
    if ls == []:                            # if ls is an empty list
        return []                           # return it
    else:
        pivot = ls[0]
        lesser = [x for x in ls[1:] if x < pivot] 
        greater = [x for x in ls[1:] if x >= pivot]
        return minSort(lesser) + [pivot] + minSort(greater)

def minu(ls):
    car = minSort(ls)                       # Sorts the list ls through minSort
    newls = []                              # new empty list
    for i in ls:                            # iterates through ls
        if i == car[0]:                     # if the number in question is equal to the lowest number in the list car                                
            newls += []                     # add nothing
        else:
            newls += [i]                    # add the number in question to the new list newls
    print car[0], newls                     # print the lowest number and a list with the remaining numbers

# SUBTASK C

def combine(list1,list2):
    addls = []                              # new empty list addls
    for i in list1:                         # iterates through the first list
        addls += [i]                        # add the number in question to the new list addls
    for c in list2:                         # iterates through the second list
        addls += [c]                        # add the number in question to the new list addls
    car = minSort(addls)                    # sorts the list addls and assigns it to variable car
    return car

def merge(a,b):
    coon = combine(a,b)                     # combines and sorts the 2 lists, assigning the new list to coon
    add2ls = []                             # new empty list add2ls
    cnt = 0
    for i in coon:                          # iterates through the list
        #cnt += 1
        if i == coon[cnt-1]:                # if the number in question is equal to the next number in coon
            add2ls += []                    # add nothing
        else:
            add2ls += [i]                   # add the number in question to list add2ls
        cnt += 1
    print add2ls
    
# TASK 2

# SUBTASK A
    
def frequency(txt):
    lowa = list(txt.lower())                # create a list from the entry
    for i in lowa:                          # search for spaces
        if i == ' ':
            lowa.remove(i)                  # remove spaces
    dic = {}                                # new empty dictionary dic
    for i in range(len(lowa)):              # make a loop that will run as many times = to the length of the list
        if lowa[i] in dic:                  # if the letters are already in the dictionary
            dic[lowa[i]] += 1               # add 1
        else:
            dic[lowa[i]] = 1                # enter into dic with a value of 1 because it is the first of that letter
    return dic

# SUBTASK B

def alpha(txt):
    dic2 = {}                               # new empty dictionary dic2
    for i in txt:                           # iterate through the inputted list txt
        if i == ' ':                        
            car = txt.split()               # create a new element within the list
    for word in car:                        # iterate through every element/word in car
        if word[0] in dic2:                 # if the first letter of each word is in the dictionary
            dic2[word[0]].append(word)      # append that word
        else:
            dic2[word[0]] = [word]          # if first letter not in dictionary create a new definition
    print dic2

# SUBTASK C

import urllib
def index():
    car = urllib.urlopen('http://introcs.cs.princeton.edu/java/data/mobydick.txt')
    dic = {}
    for line in car:
        line = line.strip('\r\n')           # Strip blank Lines
        line = line.lower()                 # Lowercase all
        line = line.translate(None, '-,.!:;"?/@%&') # Remove punctuation
        if len(line) > 1:                   
            for z in line:                  # Iterate for spaces
                if z == ' ':            
                    lscar = line.split()    # Create a new element  
                    for word in lscar:      # Iterate through all elements            
                        if len(word) > 9:   # Only add words with > 9 letters for efficiency
                            if word in dic:
                                dic[word] += 1 # Add 1 to value if the key already exists
                            else:
                                dic[word] = 1 # Create a new key of word with value 1 
        else:
            dic[line] = 1                   # If the line is 1 word, add it to the dictionary
    print dic

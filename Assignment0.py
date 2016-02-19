#
#First Serious Assignment
#
#Austin Thiel
#CPSC230-03
#Professor Gumm
#6 September 2013
#
#This one was tough
#


import math

print "TASK 1"

print

print "Paris (The Eiffel Tower)"
print "Latitude : 48, 51, 30"
print "Longitude : 9, 12, 3"

print

print "LATITUDE"
latD = input("Enter Degrees: ")
latM = input("Enter Minutes: ")
latS = input("Enter Seconds: ")

latDeg = latD + ((latM*60)+latS)/3600
latRad = latDeg*((2*math.pi)/360)

print

print "LONGITUDE"
lonD = input("Enter Degrees: ")
lonM = input("Enter Minutes: ")
lonS = input("Enter Seconds: ")

lonDeg = lonD + ((lonM*60)+lonS)/3600
lonRad = lonDeg*((math.pi)/180)

print

coord = latRad,lonRad
print coord

print
print "============================================="
print

print "TASK 2"

print

print "Seattle"
print "Latitude : 47, 36, 35"
print "Longitude : 122, 19, 59"

print

print "Houston"
print "Latitude : 29, 45, 46"
print "Longitude : 95, 22, 59"

print

earthRad = 3959

print "LATITUDE"
aLatD = input("Enter Degrees: ")
aLatM = input("Enter Minutes: ")
aLatS = input("Enter Seconds: ")

aLatDeg = aLatD + ((aLatM*60)+aLatS)/3600
aLatRad = aLatDeg*((math.pi)/180)

print

print "LONGITUDE"
aLonD = input("Enter Degrees: ")
aLonM = input("Enter Minutes: ")
aLonS = input("Enter Seconds: ")

aLonDeg = aLonD + ((aLonM*60)+aLonS)/3600
aLonRad = aLonDeg*((math.pi)/180)

dLat = aLatRad - latRad
dLon = aLonRad - lonRad

a = math.sin(dLat/2)**2 + math.cos(latRad) * math.cos(aLatRad) * math.sin(dLon/2)**2
c = 2 * math.asin(math.sqrt(a))
mi = earthRad * c

print

print mi

print

#This program only computes one distance from Paris to
#the users choice of secondary location. However, I ran
#the computations for both Seattle and Houston, and wrote them
#below. I hope this is okay.

print "The distance from Paris to Seattle is : 4738.74904893 miles"
print "The distance from Paris to Houston is : 4584.80145054 miles"
print "Paris is closer to Houston than Seattle"




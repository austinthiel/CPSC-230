##
## Austin Thiel
## Professor Gumm
## CPSC230-03
## 
## "Oh my god"
##

import urllib
import math
import webbrowser

## Task 3

## Grabs the updated file from the web and removes lines that do not contain data

quakeFile = urllib.urlopen("http://earthquake.usgs.gov/earthquakes/catalogs/eqs1day-M0.txt")
quakeFile.readlines(1)
quakeFile.readline()

## Task 1

## Prints all the data without extra spaces or lines
## (Task 1 will NOT run together with task 2/4, comment out the program you don't want to run)

##i = 0
##for line in quakeFile:
##    i+=1
##    line = line.strip('\r\n')
##    print line

## Task 2 and Task 4

## Prints only certain lat/lon/mag, plots them on a map, and opens the map in a web browser
## (Task 2/4 will NOT run together with task 1, comment out the program you don't want to run) 

def distance(aLatDeg, aLonDeg):
    
    earthRad = 6371

    latRad = 33.803056*((math.pi)/180)
    lonRad = -117.8325*((math.pi)/180)

    aLatRad = aLatDeg*((math.pi)/180)
    aLonRad = aLonDeg*((math.pi)/180)

    dLat = aLatRad - latRad
    dLon = aLonRad - lonRad

    a = math.sin(dLat/2)**2 + math.cos(latRad) * math.cos(aLatRad) * math.sin(dLon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = earthRad * c

    return km

mapUrl = "http://maps.googleapis.com/maps/api/staticmap?size=512x512&sensor=false&zoom=8&&center=33.8,-117.8"
one_degree = 111.32 #Kilometers
i = 0
for lines in quakeFile:
    i+=1
    lines = lines.strip('\r\n').split(',')
    if float(lines[8]) >= 1.0 and distance(float(lines[6]),float(lines[7])) <= 400 :
        print lines[6:9]
    if distance(float(lines[6]),float(lines[7])) <= one_degree:
        if float(lines[8]) < 1.5:
            mapUrl += "&markers=size:tiny|color:green|" + str(lines[6]) + "," + str(lines[7])
        elif 1.5 <= float(lines[8]) < 3.0:
            mapUrl += "&markers=size:small|color:yellow|" + str(lines[6]) + "," + str(lines[7])
        elif 3.0 <= float(lines[8]) < 4.5:
            mapUrl += "&markers=size:mid|color:orange|" + str(lines[6]) + "," + str(lines[7])
        elif float(lines[8]) >= 4.5:
            mapUrl += "&markers=size:normal|color:red|" + str(lines[6]) + "," + str(lines[7])

webbrowser.open(mapUrl)

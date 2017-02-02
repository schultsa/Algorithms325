import random
import sys
import os
import math


############################################################
# This section is for putting the numbers from the file into an array
############################################################
class Point:
    x = 0;
    y = 0;

    def __init__(self, x, y):
        self.x = x
        self.y = y
def distance(pointa, pointb):
    dis = math.sqrt((pointa.x-pointb.x)**2+(pointa.y-pointb.y)**2)
    return dis

def printArray(array):
    for n in range(0, len(array)):
        print(array[n].x, array[n].y)
file = open(sys.argv[1], "r+")
text = file.read()
numberOfPairs = text.count('\n')
array = []

i = 0
x = float
y = float
xstring = ""
ystring = ""

num = 0
xcoor = True

while(num<len(text)):
    if((text[num].isdigit() or text[num] == '.') and xcoor):
        xstring+=(text[num])
        if(text[num+1] == ' ' or text[num+1] == '\n'):
            xcoor = False
            x = float(xstring)
    else:
        if ((text[num].isdigit() or text[num] == '.') and not(xcoor)):
            ystring+=(text[num])
            if (text[num+1] == '\n' or text[num+1]==' '):
                xcoor = True
                y = float(ystring)
                array.append(Point(x,y))
                xstring = ""
                ystring = ""

    num += 1


############################################################
# This section is the algorithm
############################################################

m = 1000000000000.0
dis = float
arrayOfMins = []

for f in range(0, numberOfPairs):
    for s in range(f, numberOfPairs):
        if(not(f ==s)):
            dis = math.sqrt((array[f].x-array[s].x)**2+(array[f].y-array[s].y)**2)
            if dis == m:
                arrayOfMins.append(array[f])
                arrayOfMins.append(array[s])
            if dis < m:
                arrayOfMins[:] = []
                arrayOfMins.append(array[f])
                arrayOfMins.append(array[s])
                m = dis

file = open("BruteForce_output.txt","w")
t = distance(arrayOfMins[0], arrayOfMins[1])
distance1 = str(t)
distance1+='\n'
file.write(distance1)
for n in range(0, len(arrayOfMins)):
    stringToWrite = str(arrayOfMins[n].x)
    stringToWrite+= " "
    stringToWrite+= str(arrayOfMins[n].y)
    stringToWrite+='\n'
    file.write(stringToWrite)

print(distance(arrayOfMins[0], arrayOfMins[1]))

for n in range(0, len(arrayOfMins)):
    print(arrayOfMins[n].x, arrayOfMins[n].y)



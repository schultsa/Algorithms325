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


file = open("input.txt", "r+")
text = file.read()
numberOfPairs = text.count('\n')+1
array = []

i = 0
x = 0
y = 0

for m in range(0, numberOfPairs):
    if (text[(i+1)] == ' ') and (text[i].isdigit()):
        x = int(text[i])
        i +=1

    if (text[i] == ' '):
        i += 1
    if (text[i].isdigit()):
        y = int(text[i])
        i += 1


    if(i<len(text)):
        if (text[i] == ' '):
            i += 1
    if (i < len(text)):
        if(text[i] == '\n'):
            i+=1
    if (i < len(text)):
        if (text[i] == ' '):
            i += 1

    array.append(Point(x,y))

for n in range(0, numberOfPairs):
    print(array[n].x, array[n].y)

############################################################
# This section is the algorithm
############################################################

minimum = 100
distance = int
arrayOfMins = []

for f in range(0, numberOfPairs):
    for s in range(f, numberOfPairs):
        if(not(f ==s)):
            distance = math.sqrt((array[f].x-array[s].x)**2+(array[f].y-array[s].y)**2)
            if distance == minimum:
                arrayOfMins.append(array[f])
                arrayOfMins.append(array[s])
            if distance < minimum:
                arrayOfMins[:] = []
                arrayOfMins.append(array[f])
                arrayOfMins.append(array[s])
                minimum = distance

print(distance)

for n in range(0, len(arrayOfMins)):
    print(arrayOfMins[n].x, arrayOfMins[n].y)



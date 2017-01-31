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
# print("Original Array:\n")
# for n in range(0, numberOfPairs):
#     print(array[n].x, array[n].y)

############################################################
# This section is the merge sort algorithm
############################################################
# sort by gives an option of being sorted by x or y coordinate
def MergeSort(arrayOfpairs, sortBy):
    left = []
    right = []

    if(len(arrayOfpairs)==1):
        return arrayOfpairs
    mid = int(len(arrayOfpairs)/2)

    #split array into two parts and call MergeSort on both
    for n in range(0, mid):
        left.append(arrayOfpairs[n])

    for n in range(mid, len(arrayOfpairs)):
        right.append(arrayOfpairs[n])

    s = combine(MergeSort(left, sortBy), MergeSort(right, sortBy), sortBy)

    return s


        # for n in range(0, len(left)):
        #     print(left[n].x, left[n].y)
def combine (left, right, sortBy):

    if sortBy == 'x':
        combo = []

        while (len(left) > 0) and (len(right) > 0):
            if (left[0].x >= right[0].x):
                combo.append(right[0])
                # for n in range(0, len(combo)):
                #     print(combo[n].x, combo[n].y)

                del right[0]
            else:
                if (left[0].x < right[0].x):
                    combo.append(left[0])
                    # for n in range(0, len(combo)):
                    #     print(combo[n].x, combo[n].y)

                    del left[0]
        if not(len(left)== len(right)):
            if len(left) == 0:
                lenright = len(right)

                for m in range(0, lenright):
                    combo.append(right[0])
                    del right[0]
             #   n = left(left)
            if len(right) == 0:
                lenleft = len(left)
                for m in range(0, lenleft):
                    combo.append(left[0])
                    del left[0]


        return combo
    if sortBy == 'y':
        combo = []

        while (len(left) > 0) and (len(right) > 0):
            if (left[0].y >= right[0].y):
                combo.append(right[0])
                # for n in range(0, len(combo)):
                #     print(combo[n].x, combo[n].y)

                del right[0]
            else:
                if (left[0].y < right[0].y):
                    combo.append(left[0])
                    # for n in range(0, len(combo)):
                    #     print(combo[n].x, combo[n].y)

                    del left[0]
        if not(len(left)== len(right)):
            if len(left) == 0:
                lenright = len(right)

                for m in range(0, lenright):
                    combo.append(right[0])
                    del right[0]
             #   n = left(left)
            if len(right) == 0:
                lenleft = len(left)
                for m in range(0, lenleft):
                    combo.append(left[0])
                    del left[0]


        return combo

#sorted = MergeSort(array, 'x')
# print("Sorted Array:\n")
# for n in range(0, len(sorted)):
#     print(sorted[n].x, sorted[n].y)

# array = [Point(0,0),Point(1,7),Point(1,8),Point(4,0),Point(5,5)]
# sorted = MergeSort(array, 'y')
# for n in range(0, len(sorted)):
#     print(sorted[n].x, sorted[n].y)
############################################################
# This section is the find closest pair algorithm
############################################################


def distance(pointa, pointb):
    dis = math.sqrt((pointa.x-pointb.x)**2+(pointa.y-pointb.y)**2)
    return dis

def find_M_andComputeSmallestPair(left, right, min):
    L = (left[len(left)-1].x + right[0].x)/2
    M = []
    beta = distance(min[0], min[1])
    leftside = True
    rightside = True
    counter = len(left)-1
    while (leftside == True):
        if abs(left[counter].x-L) <= beta:
            M.append(left[counter])
            counter -= 1
            if(counter < 0):
                leftside = False
        else:
            leftside = False
    counter = 0
    while rightside == True:
        if abs(right[counter].x - L) <= beta:
            M.append(right[counter])
            counter += 1
            if(counter) == len(right):
                rightside = False
        else:
            rightside = False
    sortedM = MergeSort(M, 'y')
 #   minWithinL = []
    for i in range(0, len(sortedM)):
        for j in range(i, len(sortedM)):
            if not(i == j):
                if distance(sortedM[i], sortedM[j]) < beta:
                    min[:] = []
                    min.append(sortedM[i])
                    min.append(sortedM[j])
                if distance(sortedM[i], sortedM[j]) == beta:
                    min.append(sortedM[i])
                    min.append(sortedM[j])
                if distance(sortedM[i], sortedM[j]) > beta:
                    break

    return min

def findSmallest(array):
    arrayOfMins = []
    d = int
    minimum = 100000
    for f in range(0, len(array)):
        for s in range(f, len(array)):
            if (not (f == s)):
                d = distance(array[f], array[s])
                if d == minimum:
                    arrayOfMins.append(array[f])
                    arrayOfMins.append(array[s])
                if d < minimum:
                    arrayOfMins[:] = []
                    arrayOfMins.append(array[f])
                    arrayOfMins.append(array[s])
                    minimum = d

    return arrayOfMins
def closestPair(array):
    array = MergeSort(array, 'x')
    left = []
    right = []
    minleft = []
    minright = []
    minimum = []
    if (len(array) <= 3):
        minimum = findSmallest(array)
    else:
        mid = int(len(array) / 2)

        for n in range(0, mid):
            left.append(array[n])

        for n in range(mid, len(array)):
            right.append(array[n])

        minleft = closestPair(left)
        minright = closestPair(right)
        disleft = distance(minleft[0], minleft[1])
        disright = distance(minright[0], minright[1])
        if disleft<= disright:
            min = minleft
        else:
            min = minright
        minimum = find_M_andComputeSmallestPair(left,right, min)

    return minimum


arrayOfMins = closestPair(array)
print(distance)

for n in range(0, len(arrayOfMins)):
    print(arrayOfMins[n].x, arrayOfMins[n].y)





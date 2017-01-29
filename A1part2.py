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
print("Original Array:\n")
for n in range(0, numberOfPairs):
    print(array[n].x, array[n].y)

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

    sorted = combine(MergeSort(left, sortBy), MergeSort(right, sortBy), sortBy)
    return sorted


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

sorted = MergeSort(array, 'x')
print("Sorted Array:\n")
for n in range(0, len(sorted)):
    print(sorted[n].x, sorted[n].y)































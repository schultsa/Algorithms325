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


file = open(sys.argv[1], "r+")
text = file.read()
numberOfPairs = text.count('\n')

array = []
def printArray(array):
    for n in range(0, len(array)):
        print(array[n].x, array[n].y)

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

    if(len(arrayOfpairs)<=1):
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
    d = float
    minimum = 100000000000000000
    for f in range(0, len(array)):
        for s in range(f, len(array)):
            if (not (f == s)):
                d = distance(array[f], array[s])
                if d == minimum:
                    arrayOfMins.append(array[f])
                    arrayOfMins.append(array[s])
                else:
                    if d < minimum:
                        arrayOfMins[:] = []
                        arrayOfMins.append(array[f])
                        arrayOfMins.append(array[s])
                        minimum = d

    return arrayOfMins

def closestPair(array):

    min = []
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
        minright = closestPair(right)
        minleft = closestPair(left)

        disleft = distance(minleft[0], minleft[1])
        disright = distance(minright[0], minright[1])

        if len(min)>0:
            if disleft == distance(min[0], min[1]):
                for m in range(0, len(minleft)):
                    min.append(minleft[m])
            if disright == distance(min[0], min[1]):
                for m in range(0, len(minright)):
                    min.append(minright[m])
            if disleft < distance(min[0], min[1]):
                min = minleft
            if disright <distance(min[0], min[1]):
                min = minright
        else:

            if disleft < disright:
                min = minleft
            if disright < disleft:
                min = minright
            if disright == disleft:
                for n in range(0, len(minleft)):
                    min.append(minleft[n])
                for n in range(0, len(minright)):
                    min.append(minright[n])
        minimum = find_M_andComputeSmallestPair(left,right, min)

    return minimum

array = MergeSort(array, 'x')
arrayOfMins = closestPair(array)
file = open("Naive_output.txt","w")
distance1 = format(distance(arrayOfMins[0], arrayOfMins[1]))
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





import random
import sys
import os
import math



############################################################
# This section is for putting the numbers from the file into an array
############################################################
class Point:
    x = float;
    y = float;

    def __init__(self, x, y):
        self.x = x
        self.y = y

def printArray(array):
    for n in range(0, len(array)):
        print(array[n].x, array[n].y)
file = open("numbers.input", "r+")
text = file.read()
numberOfPairs = text.count('\n')
#print(numberOfPairs)
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

#printArray(array)
# for m in range(0, numberOfPairs):
#     if (text[(i+1)] == ' ') and (text[i].isdigit()):
#         x = int(text[i])
#         i +=1
#
#     if (text[i] == ' '):
#         i += 1
#     if (text[i].isdigit()):
#         y = int(text[i])
#         i += 1
#
#
#     if(i<len(text)):
#         if (text[i] == ' '):
#             i += 1
#     if (i < len(text)):
#         if(text[i] == '\n'):
#             i+=1
#     if (i < len(text)):
#         if (text[i] == ' '):
#             i += 1
#
#     array.append(Point(x,y))
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
def containsPair(array, pointa, pointb):
    for i in range(0, len(array)):
        if((array[i].x == pointa.x and array[i].y == pointa.y) and (array[i+1].x== pointb.x) and(array[i+1].y== pointb.y)):
            return True
        else:

            if ((array[i].x == pointb.x and array[i].y == pointb.y) and (array[i + 1].x == pointa.x) and (
                array[i + 1].y == pointa.y)):
                return True
        i+=1

    return False
def distance(pointa, pointb):
    dis = math.sqrt((pointa.x-pointb.x)**2+(pointa.y-pointb.y)**2)
    return dis

def find_M_andComputeSmallestPair(leftx, rightx, min, arrayy):
    L = (leftx[len(leftx)-1].x + rightx[0].x)/2
    M = []
    beta = distance(min[0], min[1])

    for n in range(0, len(arrayy)):
        if abs(arrayy[n].x-L) <= beta:
            M.append(arrayy[n])


    for i in range(0, len(M)):
        for j in range(i, len(M)):
            if not(i == j):
                if distance(M[i], M[j]) < distance(min[0], min[1]):
                    min[:] = []
                    min.append(M[i])
                    min.append(M[j])

                if distance(M[i], M[j]) == distance(min[0], min[1]):
                    if not(containsPair(min, M[i], M[j])):
                        min.append(M[i])
                        min.append(M[j])
                        print("------- mins")
                        for n in range(0, len(min)):
                            print(min[n].x, min[n].y)
                        print("------- mins")
                if distance(M[i], M[j]) > beta:
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

def closestPair(arrayx, arrayy):
  #  array = MergeSort(array, 'x')
    min = []
    leftx = []
    rightx = []
    lefty = []
    righty = []
    minleft = []
    minright = []
    minimum = []
    if (len(arrayx) <= 3):

        minimum = findSmallest(arrayx)
    else:
        midx = int(len(arrayx) / 2)
        midy = int(len(arrayy)/2)

        for n in range(0, midx):
            leftx.append(arrayx[n])

        for n in range(midx, len(arrayx)):
            rightx.append(arrayx[n])
        middlexvalue = arrayx[midx].x

        for n in range(0, len(arrayy)):
            if(arrayy[n].x<= middlexvalue):
                lefty.append(array[n])
            else:
                righty.append(array[n])
        # the above for loop is step 2 in email

        minright = closestPair(rightx, righty)
        minleft = closestPair(leftx, lefty)

        disleft = distance(minleft[0], minleft[1])
        disright = distance(minright[0], minright[1])

        if len(min)>0:
            if(disleft< disright):
                if(disleft==distance(min[0], min[1] )):
                    for m in range(0, len(minleft)):
                        if (not (containsPair(min, minleft[m], minleft[m+1]))):
                            min.append(minleft[m])
                            min.append(minleft[m+1])
                            m+=1
                        m+=1
                if disleft < distance(min[0], min[1]):
                    min[:] = []
                    min = minleft

            if(disleft > disright):
                if (disright == distance(min[0], min[1])):
                    for m in range(0, len(minright)):
                        if (not (containsPair(min, minright[m], minright[m + 1]))):
                            min.append(minright[m])
                            min.append(minright[m + 1])
                            m += 1
                        m+=1
                if disright< distance(min[0], min[1]):
                    min[:] = []
                    min = minright
            if(disleft == disright):
                if (disright == distance(min[0], min[1])):
                    for m in range(0, len(minright)):
                        if (not (containsPair(min, minright[m], minright[m + 1]))):
                            min.append(minright[m])
                            min.append(minright[m + 1])
                            m += 1
                        m+=1
                if disright< distance(min[0], min[1]):
                    min = minright
                if (disleft == distance(min[0], min[1])):
                    for m in range(0, len(minleft)):
                        if (not (containsPair(min, minleft[m], minleft[m + 1]))):
                            min.append(minleft[m])
                            min.append(minleft[m + 1])
                            m += 1
                        m += 1
                if disleft< distance(min[0], min[1]):
                    min[:] = []
                    min = minleft

            if disleft == distance(min[0], min[1]):
                for m in range(0, len(minleft)):
                    if (not (containsPair(min, minleft[m], minleft[m+1]))):
                        min.append(minleft[m])
                        min.append(minleft[m+1])
                        m+=1
                    m+=1

            # if disright == distance(min[0], min[1]):
            #     for m in range(0, len(minright)):
            #         if (not(containsPair(min, minright[m], minright[m+1]))):
            #             min.append(minright[m])
            #             min.append(minright[m+1])
            #             m+=1
            #
            # if disleft < distance(min[0], min[1]):
            #     min = minleft
            # if disright <distance(min[0], min[1]):
            #     min = minright
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
        minimum = find_M_andComputeSmallestPair(leftx,rightx, min, arrayy)

    return minimum

arrayx = MergeSort(array, 'x')
arrayy = MergeSort(array,'y')
arrayOfMins = closestPair(arrayx,arrayy)

file = open("Enhanced_output.txt","w")
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

# p1 = Point(1,2)
# p2 = Point(3,4)
# p3 = Point(5,6)
# p4 = Point(7,8)
# arraya = [Point(7,8),Point(7,8), Point(3,4),Point(1,2)]
# if(containsPair(arraya, p1,p2)):
#     print("contains")

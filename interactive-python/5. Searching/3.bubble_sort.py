def bubbleSort(aList):
    for passNum in range(len(alist) - 1, 0, -1):
        for i in range(passNum):
            if aList[i] > aList[i + 1]:
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

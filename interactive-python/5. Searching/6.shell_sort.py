def shellSort(aList):
    subListCount = len(aList) // 2
    while subListCount > 0:

        for startPosition in range(subListCount):
            gapInsertionSort(aList, startPosition, subListCount)

        print("After increments of size", subListCount, "The list is", aList)

        subListCount = subListCount // 2


def gapInsertionSort(aList, start, gap):
    for i in range(start + gap, len(aList), gap):

        currentValue = aList[i]
        position = i

        while position >= gap and aList[position - gap] > currentValue:
            aList[position] = aList[position - gap]
            position = position - gap

        aList[position] = currentValue


aList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(aList)
print(aList)

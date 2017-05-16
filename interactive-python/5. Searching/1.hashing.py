def hash(aString, tableSize):
    sum = 0
    for pos in range(len(aString)):
        sum = sum + ord(aString[pos])

    return sum % tableSize


print hash("hello", 5)

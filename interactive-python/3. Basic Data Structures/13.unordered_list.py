class Node:
    def __init__(self, initialdata):
        self.data = initialdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def seData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList():

    def __init__(self):
        self.head = None

    def isEmpty():
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()

# SPECIAL CASE OF MODIFIED VALUE = HEAD
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        previous = None
        temp = Node(item)
# HELP FROM GITHUB REPO --> USING NODE(ITEM), I WAS SETTING GET NEXT TO A
# REGULAR PARAMETER, WHEN IT NEEDED TO BE A NODE!
        while current is not None:
            previous = current
            current = current.getNext()

        previous.setNext(temp)


myList = UnorderedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)

print(myList.size())
print(myList.search(93))
print(myList.search(100))

myList.add(100)
print(myList.search(93))
print(myList.search(100))

myList.remove(54)
print(myList.size())
myList.remove(93)
print(myList.size())

myList.append(1)
print(myList.size())

import pythonds
from pythonds.basic.stack import Stack

#  Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(myStr):
    s = Stack()
    for ch in myStr:
        s.push(ch)

    emptyStr = ""

    i = 0
    while i < s.size():
        emptyStr = emptyStr + s.pop()

    return emptyStr



hello = revstring("Hello")
awkward = revstring("awkward")

print(hello)
print(awkward)

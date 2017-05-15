i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers

    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num


# Study Drills
def while_function(limit):
    i = 0
    numbers = []

    for i in range(i, limit):  # rewrite while loop to for loop
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers

        print "At the bottom i is %d" % i


print "\nFunction conversion test\n"
while_function(10)

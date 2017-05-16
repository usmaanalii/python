aName = input("Please enter your name ")

print("Your name in all capitals is",
      aName.upper(), "and has length", len(aName))

sage = input("What is your age? ")
age = int(sage)
print("Your age is", age, "and in five years you will be",
      (age + 5), "years old \n")

# FORMATTED STRINGS !!

# These are formatted strings which enable more control over output 'look'
# The variables need to be defined prior to creation!
print("Hello", "World", end="_")

print(aName, "is", age, "years old")

# % is called the format operator,
# %d specifies integer whereas %s specifies string
print("%s is %d years old" % (aName, age))

# Examples of modifiying the format operators for margin and float inputs
price = 24
item = "banana"
print("The %s costs %d pence" % (item, price))

print("The %-20s costs %0.2f pence" % (item, price))

itemdict = {"item": "banana", "price": 24}
print("The %(item)s costs %(price).2f pence" % itemdict)

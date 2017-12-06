import array
from collections import namedtuple

# * List comprehensions and generator expressions

# ** List comprehensions and readability

# Example 2.1 - Build a list of Unicode codepoints from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

codes  # [36, 162, 163, 165, 8364, 164]

# Example 2.2 - Build a list of Unicode codepoints from a string, take two
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes  # [36, 162, 163, 165, 8364, 164]

# ** Listcomps versus map and filter

# Example 2.3 - The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii  # [162, 163, 165, 8364, 164]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii  # [162, 163, 165, 8364, 164]

# ** Cartesian products

# Example 2.4 - Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]
tshirts

# ** Generator expressions

# Example 2.5 - Initializing a tuple and an array from a generator expressions
symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols)
array.array('I', [36, 162, 163, 165, 8364, 164])  # 'I' - storage type

# Example 2.6 - Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

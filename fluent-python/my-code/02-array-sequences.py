# Chapter 2. An array of sequences  NOQA
import array
from collections import namedtuple

# * List comprehensions and generator expressions

# ** List comprehensions and readability

# Example 2.1 - Build a list of Unicode codepoints from a string
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

codes

# Example 2.2 - Build a list of Unicode codepoints from a string, take two
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes

# ** Listcomps versus map and filter

# Example 2.3 - The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii

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

# ** Tuples are not just immutable lists

# ** Tuples as records

# Example 2.7 - Tuples used as records
lax_coordinates = (33.9435, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s%s' % passport)

for country, _ in traveler_ids:
    print(country)

# ** Tuple unpacking
lax_coordinates = (33.9435, -118.408056)
latitude, longitude = lax_coordinates
latitude
longitude

divmod(20, 8)

t = (20, 8)
divmod(*t)

quotient, remainder = divmod(*t)
quotient, remainder

# ** Using * to grab excess items
a, b, *rest = range(5)
a, b, rest
a, b, *rest = range(3)
a, b, rest
a, b, *rest = range(2)
a, b, rest

a, *body, c, d = range(5)
a, body, c, d

*head, b, c, d = range(5)
head, b, c, d

# ** Nested tuple unpacking

# Example 2.8 - Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# ** Named tuples

# Example 2.9 - Defining and using a named tuple type
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo
tokyo.population
tokyo.coordinates

# Example 2.10 - Named tuple attributes and methods
City._fields
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()

for key, value in delhi._asdict().items():
    print(key + ':', value)

# * Slicing
#   - Useful for splitting in half

# ** Why slices and range exclude the last item
list_example = [10, 20, 30, 40, 50, 60]
list_example[:2]
list_example[2:]

# ** Slice objects
#   - list[a:b:b] provides a 'step' to skip
string_example = 'bicycle'

string_example[::3]
string_example[::-1]
string_example[::-2]

# Example 2.11 - Line items from a flat file invoice
invoice = """
0.....6.................................40........52...55........
... 1909 Pimoroni PiBrella $17.50 3 $52.50
... 1489 6mm Tactile Switch x20 $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201 $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# ** Multi-dimensional slicing and ellipsis
#   - Mainly used in numpy for example [1:3, 2:4] for x, y axis

# ** Assigning to slices
list_example_2 = list(range(10))
list_example_2
list_example_2[2:5] = [20, 30]
list_example_2

del list_example_2[5:7]
list_example_2

list_example_2[3::2] = [11, 22]
list_example_2

list_example_2[2:5] = 100  # TypeError: can only assign an iterable
list_example_2

# ** Using + and * with sequences
list_example_3 = [1, 2, 3]
list_example_3 * 5

5 * 'abcd'

# ** Building lists of lists

# Example 2.12 - A list with 3 lists of length 3 can represent Tic-tac-toe
board = [['_'] * 3 for i in range(3)]
board
board[1][2] = 'X'
board

# Example 2.13 - A list with three references to the same list is useless
#   - The same 'row' is appended 3 times
weird_board = [['_'] * 3] * 3
weird_board
weird_board[1][2] = 'O'
weird_board

# ** Augmented assignment with sequences
#   - Regers tp += and *= (e.g in-place addition)
list_example_4 = [1, 2, 3]
id(list_example_4)

list_example_4 *= 2
list_example_4
id(list_example_4)  # same as before

tuple_example = (1, 2, 3)
id(tuple_example)

tuple_example *= 2
id(tuple_example)  # not the same as before

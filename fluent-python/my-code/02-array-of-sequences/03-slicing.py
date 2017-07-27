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

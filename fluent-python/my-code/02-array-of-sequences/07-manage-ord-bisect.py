# * Managing ordered sequences with bisect
import bisect
import sys
import random

#   - two main functions bisect and insort, both use the binary search
#   algorithm for finding and inserting into sorted sequences

# ** Searching with bisect
#   - bisect(haystack, needle)
#   - insort finds the place to insert to maintain order and inserts
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '   |'
        print(ROW_FMT.format(needle, position, offset))


demo(bisect.bisect_left)

demo(bisect.bisect)

# - bisect right and left will insert the value either side of the insert point
# - you can specify start and end points for Searching

# - Table lookups by numeric values, convert test scores to grades


# Example 2.18 - Given a test score, grade returns the corresponding
#                letter grade
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]

# ** Inserting with bisect.insort
#   - insort(seq, item) inserts item into seq, keeping it in ascnding order

# Example 2.19 - Insort keeps a sorted sequence always sorted
SIZE = 7
random.seed(1 / 29)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

# If you are using lists of numbers, arrays are the way to go!

# * When a list is not the answer
import numpy
from array import array
from random import random
from time import perf_counter as pc
from collections import deque
#   - Arrays will be better for storing millions of floating points
#   since they hold bytes not the fully fledged values
#   - Also deque's might work better if your adding/removing from start/end
#   frequently

# ** Arrays
#   - array.array is more efficient for storing numbers
#   - They are based on C arrays and are very fast

# Example 2:20 - Creating, saving and loading a large array of floats
#   - 'd' double precision floats
floats = array('d', (random() for i in range(10 ** 2)))
floats[-1]

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # save to binary file
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 2)
fp.close()

floats2[-1]

floats2 == floats

# ** Memory views
#   - Important if your doing a lot of work with arrays
#   - Concept of sharing memory between data structures without copying

# Example 2:21 - Changing the value of an array item by poking one of its
#                bytes
numbers = array('h', [-2, -1, 0, 1, 2])  # 'h' - short signed integers
memv = memoryview(numbers)
len(memv)

memv[0]

memv_oct = memv.cast('B')  # 'B' unsigned char
memv_oct.tolist()
memv_oct[5] = 4

numbers

# ** NumPy and SciPy
#   - Advanced array and matrix operations
#   - Hold multidimensional, homogeneous arrays and matrix types
#   efficient at elementwise operations

# Example 2:22 - Basic operations with rows and columnds in a numpy.ndarray
a = numpy.arange(12)
a
type(a)
a.shape
a.shape = 3, 4
a
a[2]
a[2, 1]
a[:, 1]
a.transpose()

# ** Deques and other queues
#   - Inserting and removing from index 0 is costly since the entire list
#   needs to be shifted
#   - collections.deque is thread safe and double ended
#   - perfect for "last seen items" since you can specify a max length
dq = deque(range(10), maxlen=10)
dq

dq.rotate(3)
dq

dq.rotate(-4)
dq

dq.appendleft(-1)
dq

dq.extend([11, 22, 33])
dq

dq.extendleft([10, 20, 30, 40])  # appends iteratively so its reversed in dq
dq

# * Byte essentials
import array
import struct
#   - binary seq. types unlike Python 2 str
#   - Two types of built in binary seq. types exist
#       1. immutbale bytes
#       2. mutable bytearray
#   - Each item in ^ is an integer from 0-255

# %% Example 4.2 - A 5 byte seq. as bytes and bytearray
cafe = bytes('cafe', encoding='utf_8')
cafe

cafe[0]
cafe[:1]

cafe_arr = bytearray(cafe)
cafe_arr

cafe_arr[-1:]

# Binary seq. has a class method *fromhex* that str doesnt have
bytes.fromhex('31 4B CE A9')

# %% Example 4.3 - Initializing bytes from the raw data of an array
#   - 'h' -> short integers (16 bits)
#   - octets hold copy of the bytes that make up the numbers
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

# ** Structs and memory views
#   - struct module -> functions to parse packed bytes into a tuple of fields
#   of different types and to perform the opposite conversion
#   (tuple -> bytes)
#   - memoryview -> provides shared memory access to slices of data

# %% Example 4.4 - Using memoryview and struct to inspect a GIF image header
fmt = '<3s3sHH'

with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
bytes(header)

struct.unpack(fmt, header)

del header
del img

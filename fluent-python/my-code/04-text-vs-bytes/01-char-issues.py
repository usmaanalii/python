# Text Versus Bytes
#   - Python 3 changed strings of human text and seq. of raw bytes
#   - No longer implicitly convert between the two

# * Character issues
#   - string -> sequence of characters (but what is a character)
#   - characters -> unicode characters
#   - Unicode character -> identity is a code point (0 to 1_114_111 (base 19))
#   - Bytes -> depend on the encoding (alg. to convert code points to
#   byte seq. and vice-versa), e.g utf-8

#   - encoding -> code points to bytes
#   - decoding -> bytes to code points

# %% Example 4.1 - Encoding and decoding
s = 'cafe'
len(s)

b = s.encode('utf8')
b

len(b)

b.decode('utf8')

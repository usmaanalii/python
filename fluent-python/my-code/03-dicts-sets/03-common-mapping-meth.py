# * Overview of common mapping methods
import sys
import re
import collections
#   - dict's most useful variations include defultdict and OrderedDictt

# ** Handling missing keys with setdefault
#   - d[k] raises an error when k is not a key
#   - updating items using get() is inefficient

# %% Example 3.2 - index0.py uses dict.get to fetch and update a list of
#                  word occurences from the index
WORD_RE = re.compile('\w+')

index = []
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly to make a point
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# %% Example 3.4:  index.py uses dict.setdefault to fetch and update a list
#                  of word occurences from the index in a single line

WORD_RE = re.compile('\w+')

index = []
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

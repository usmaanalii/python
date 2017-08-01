# * Mappings with flexible key lookup
import re
from collections import defaultdict
# ** defaultdict: another take on missing keys
#   - Adding a nonexisting key to defaultdict(list) does the following
#       1. Calls list() to create a new list
#       2. Inserts the list into the defaultdict using 'new key' as key
#       3. Returns a reference to that list

# Example 3.5 - index.py uses dict.setdefault to fetch and update a list of
# word occurenced from the index in a single line
WORD_RE = re.compile('\w+')

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])

# ** The __missing__ methods
#   - called by __getitem__ for the dict[key] operator


# %% Example 3.6/3.7 - When searching for a non-string key
#   - StrKeyDict0 converts it to str when its not found
class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# Tests for item retrieval using 'd[key]' notation
d = StrKeyDict0([('2', 'two'), ('4', 'four')])
d['2']
d[4]
d[1]

# Tests for item retrieval using 'd.get(key)' notation
d.get('2')
d.get(4)
d.get(1, 'N/A')

2 in d
1 in d

#   - Searching for k in ny_dict.keys() is efficient in Python 3 beccause
#   dict.keys() returns a view (not a list like Python 2)

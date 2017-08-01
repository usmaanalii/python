# Dictionaries and Sets
from collections import abc
#   - Hash tables are the engines behind dicts
#   - Sets are implemented with hash tables too

# * Generic mapping types
my_dict = {}
isinstance(my_dict, abc.Mapping)

# %% hashable
#   - the keys must be hashable (limitation of all mapping types)
#   - hashable
#       o object has a hash value which never changes during its lifetime
#       o str, byte and numeric types are hashable
#       o all immutable objects are hashable (tuples are but can hold
#       reference to mutable objects)
tt = (1, 2, (30, 40))
hash(tt)

tl = (1, 2, [30, 40])
hash(tl)  # error unhashable list

tf = (1, 2, frozenset([30, 40]))
hash(tf)

# %% Ways of building dicts
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})
a == b == c == d == e

# We can also use *dict comprehension" to build them

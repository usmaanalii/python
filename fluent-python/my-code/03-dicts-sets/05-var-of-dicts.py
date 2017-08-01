# * Variations of dict
from collections import Counter
#   - collections.OrderedDict
#       o insertion order is maintained
#       o .popitem([last=true])
#   - collections.chainMap
#       o list of mappings that can be searched as one
#       o if value exists in all keys?
#   - collections.Counter
#       o holds integer count for each key
#       o most_common([n])
#   - collections.UserDict
#       o pure python dict implementiation
#       o designed for subclassing

# %% Counter
ct = Counter('abracadabra')
ct
ct.update('aaaaazzzz')
ct
ct
ct.most_common(2)

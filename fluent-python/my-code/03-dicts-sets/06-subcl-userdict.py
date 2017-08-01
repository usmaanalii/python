# * Subclassing UserDict
from collections import UserDict
#   - Easier to create new mapping types by extending UserDict than dict
#   - Does not inherit from dict
#   - Example will
#       o Store all keys as str


# %% Example 3.8 - StrKeyDict always converts non-string keys to str on
#                  insertion, update and lookup
class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# MutableMapping
#   - .update
#       o used by __init__ to load the instance from other mappings
#       o uses self[key] = value so calls __setitem__
# Mapping
#   - .get 

# * Immutable mappings
from types import MappingProxyType
# 	- All mappings provided are mutable, immutable will prevent changes
# 	from key value mappings

# %% Example 3.9 - MappingProxyType builds a read only mappingproxy instance
#                  from a dict
d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy
d_proxy[1]

d_proxy[2] = 'x'  # TypeError (no assignment)

d[2] = 'B'
d_proxy
d_proxy[2]

# Items can be seen through d_proxy but NOT made through d_proxy
# It is dynamic, so changes in d are reflected in d_proxy

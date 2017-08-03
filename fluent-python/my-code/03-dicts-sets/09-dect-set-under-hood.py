# * dict and set under the hood
# 	- How efficient are they?
# 	- Why unordered?
# 	- Why are keys and set elements restricted to certain objects?
# 	- Why is order dep. on insertion order (and why can it change)
# 	- Why is it bad to add items whilst ierating through it

# %% A performance experiment
# 	- Check the effect of size when using *in*

# Example 3.14 - Search for needles in haystack
found = 0
for n in needles:
    if n in haystack:
        found += 1

# Example 3.15 - Use set intersection to count the needles in haystack
found = len(needles & haystack)

# Results from the tests show that dicts and sets are very speedy, whilst
# lists are slow due to lack of hashing

# ** Hash tables in dictionaries
#   - Hash table is a sparse array (always has empty cells)
#   - Cells often called buckets
#   - Bucket for each item, containing
#       o reference to the key
#       o reference to the value of the item
#   - Buckets are all the same size, so access is done by offset
#   - Keeps 1/3 of the buckets empty
#   - Hash value is calculated when storing an item

# ** Hashes and equality
#   - hash values must be equal in equality checks for objects
#   - hash values should scatter around the index space as much as possible

# ** The hash table algorithm
#   - my_dict[search_key]
#       o calls hash(search_key) -> hash value of search_key
#       o uses bits of the value as offset to look up a bucket
#       in the hashtable
#       o if the bucket is empty -> KeyError
#       o if successfull -> found_key:found_value pair is made
#       o checks if search_key == found_key -> returns found_value
#       0 hash collision -> search_key !=  found_key

#   - If the hash table is too crowded, a new location is used for a new table
#   - As the table grows, the no. hash bits used as bucket offsets does
#   to avoid collisions

# ** Practical consequences of how dict works
#   1. Keys must be hashable objects
#       o supports hash()
#       o supports __eq__()
#       o a == b => hash(a) == hash(b)

#   2. dicts have high overhead memory wise
#       o list of tuples over list of dicts
#       o removes overhead of
#           x one hasht table per record
#           x not storing field names again with each record
#       o __slots__ does ^^ (changes instance attributes dict to set)

#   3. Key search is very fast
#       o memory may not be great but access is!

#   4. Key ordering dep. on insertion order
#       o ??

# %% Example 3.17 - dialcodes.py -> fills three dicts w/ same data sorted in
#                   different ways
# dial codes of the top 10 most populous countries
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

d1 = dict(DIAL_CODES)
print('d1:', d1.keys())

d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())

d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print('d3:', d3.keys())

#   5. Adding items to a dict may change the order of existing keys
#       o Adding items -> hash table might grow (create bigger hash table
#       and transfer all existing items)
#       o collisions might happen during the transfer
#       o keys are likely to be ordered differently in the new table
#       o implementation dependent so can't predict the results
#       o read it first, then add, don't do at once

# ** How sets work -- practical consequences
#   - use hash tables but, each bucket only holds a reference to the element
#   - like referencing the key only
#   - before sets, dicts were used with dummy values

# ** Chapter summary
#   - defaultDict, OrderedDict, ChainMap, Counter, UserDict (for extending)
#   - setdefault -> update items holding mutable values (dict of list)
#   - update -> bulk insertion/overwriting of items
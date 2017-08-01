# * Set theory
# 	- frozenset -> immutable sibling
# 	- collection of unique objects
# 	- must be hashable (frozenset is but set isn't)
# 	- Supports infix opeators -> | & and -

# %% Use Case - Removing duplicates
set_example = ['spam', 'spam', 'eggs', 'spam']
set(set_example)
list(set(set_example))

# Email addresses (haystack), set of addresses (needles)
#   - Solve using set intersection (&)

# Example 3.10 - Count occurences needles in a haystack, both of type set
found = len(needles & haystack)

# Example 3.11 - Count occurences of needles in a haystack (long)
#   - doesnt NEED to be sets (unlike 3.19)
found = 0
for n in needles:
    if n in haystack:
        found += 1

# Example 3.12 - Count occurences needles in a haystack, solve set requirement
found = len(set(needles) & set(haystack))

# another way
found = len(set(needles).intersection(haystack))

# ** set literals

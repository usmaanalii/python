# ** Augmented assignment with sequences
#   - Regers tp += and *= (e.g in-place addition)
list_example_4 = [1, 2, 3]
id(list_example_4)

list_example_4 *= 2
list_example_4
id(list_example_4)  # same as before

tuple_example = (1, 2, 3)
id(tuple_example)

tuple_example *= 2
id(tuple_example)  # not the same as before

# ** A += assignment puzzler

# Example 2.15 - The unexpected result: item t2 is changed and an exception
# is raised
t = [1, 2, [30, 40]]
t[2] += [50, 60]
t

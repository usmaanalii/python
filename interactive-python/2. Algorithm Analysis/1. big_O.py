# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number
# on the list. O(n2).
# The second function should be linear O(n)

num_list = [5, 10, 8, 9]

# Write two Python functions to find the minimum number in a list.

# The first function should compare each number to every other number on
# the list (order n squared).


def order_nsq(array):
    lowest_value = array[0]
    for x in array:
        if x < lowest_value:
            lowest_value = x
    print(lowest_value)


order_nsq(num_list)


# The second function should be linear (order n).
def ordern(array):
    sorted_array = sorted(array)
    print(sorted_array[0])


ordern(num_list)

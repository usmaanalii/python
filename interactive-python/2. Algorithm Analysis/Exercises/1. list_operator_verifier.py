import timeit
from timeit import Timer


def list_index(list_input):
    test = list(list_input)
    return list_input.index(3)


small_test = list_index([1, 2, 3])  # RETURNS 2
large_test = list_index([1, 2, 2, 4, 5, 3])  # RETURNS 1

small_list_time = Timer("small_test", "from __main__ import small_test")
large_list_time = Timer("large_test", "from __main__ import large_test")
print("small list ", small_list_time.timeit(number=10000), "microseconds")
print("large list ", large_list_time.timeit(number=10000), "microseconds")
print("difference is  ", large_list_time.timeit(number=100000) -
      small_list_time.timeit(number=10000), "nanoseconds")

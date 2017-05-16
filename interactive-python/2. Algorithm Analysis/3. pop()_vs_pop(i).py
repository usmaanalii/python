import timeit
# Import the Timer class defined in the module
from timeit import Timer

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print("beginning : " + str(pop_zero.timeit(number=1000)))

x = list(range(2000000))
print("end : " + str(pop_end.timeit(number=1000)))

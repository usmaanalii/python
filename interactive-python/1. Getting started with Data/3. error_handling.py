# RUNTIME ERROR
import math

anumber = int(input("Please enter a number"))

if (anumber < 0):
    raise RuntimeError("Please enter a positive number")
else:
    print(math.sqrt(anumber))

# NOTES --> 1. REMEMBER TO 'RAISE' THE ERROR 2. REMEMBER THAT ELSE IS NOT
# INDENTED (SAME LEVEL AS IF)

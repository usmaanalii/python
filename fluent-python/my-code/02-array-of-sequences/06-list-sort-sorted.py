# ** list.sort abd the sorted built-in function
#   - functions or methods that change an object in place should return
#   None making it clear, that the object was modified
fruits = ['grape', 'raspberry', 'apple', 'banana']

sorted(fruits)

fruits

sorted(fruits, reverse=True)
sorted(fruits, key=len)
sorted(fruits, key=len, reverse=True)

fruits

# Changes the original fruits array
fruits.sort()
fruits

# * Handling text files
#   - Best practise -> Unicode sandwhich
#       1. Bytes to strings on input (opening a file for reading)
#       2. Meat -> business logic, text handling on str objects
#       3. Strints to bytes on output
#   - This is done implicitly on .read() and .write(text)

# %% Example 4.9 - A platform encoding issue
open('cafe.txt', 'w', encoding='utf_8').write('cafē')
open('cafe.txt').read()  # failed to specify itf-8 when reading it

# Always pass an encoding= argument whe opening text files, since
# the default may change from machine to machine, or day to day

# %% Closer inspection of 4.9
fp = open('cafe.txt', 'w', encoding='utf_8')
fp.write('cafē')
fp.close()

import os  # noqa
os.stat('cafe.txt').st_size

fp2 = open('cafe.txt')
fp2.read()
fp2.encoding

fp3 = open('cafe.txt', encoding='utf_8')
fp3
fp3.read()

fp4 = open('cafe.txt', 'rb')
fp4
fp3.read()

# ** Encoding defaults: a madhouse

# %% Example 4.11 - Exploring encoding defaults
expressions = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()u
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding
"""

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

# * Understanding encode/decode problems
#   - UnicodeEncodeError and UnicodeDecodeError's are descriptive
#     rather than UnicodeError

# ** Coping with UnicodeEncodeError
#   - If a character is not defined in the target encoding, then
#     a UnicodeError will be raised, this can be handled by custom
#     handling methods, thorugh an errors argument

# %% Example 4.6 - Encoding to bytes: success and error handling
city = 'São Paulo'
city.encode('utf_8')
city.encode('utf_16')
city.encode('iso8859_1')
city.encode('cp437')  # UnicodeEncodeError
city.encode('cp437', errors='ignore')
city.encode('cp437', errors='replace')  # uses a ?
city.encode('cp437', errors='xmlcharrefreplace')

# ** Coping with UnicodeDecodeError
#   - When converting a binary sequence to text, you will
#     get a UnicodeDecodeError when unexpected bytes are found

# %% Example 4.7 - Deocding from str to bytes: success and error handling
octets = b'Montr\xe9al'
octets.decode('cp1252')  # superset of latin1
octets.decode('iso8859_7')  # Greek
octets.decode('koi8_r')  # Russian
octets.decode('utf-8')  # UnicodeDecodeError, can't decode 0xe9

# ** SyntaxError when loading modules with unexpected encoding
#   - UTF-8 is the default source encoding for Python3 (ASCII for Python 2)
#   - Common error happens when opening a file made on Windows with cp1252

# %% Example 4.8 - 'ola.py'
print('Olá, Mundo!')

# ** How to discover the encoding of a byte sequence
#   - You can't..
#   - Say, you have a text file, but don't know its encoding
#   - Some communication protocols (HTTP, XML) have headers telling us the
#     encoding

# ** BOM: a useful gremlin
#   - b'\xff\xfe' byte-order mark or little-endian
#   - ZERO WIDTH NO-BREAK SPACE
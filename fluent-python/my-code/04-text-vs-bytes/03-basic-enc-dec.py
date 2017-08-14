# * Basic encoders/decoders
#   - Codes are encoders/decoders. Python has 100+ such as utf8 etc..

# %% Example 4.5 - The string "El Nino" enoded with three codecs
#                  producing very different byte sequences
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

# cp437 - the original character set of IBM PC
# utf-8 - Most comon 8-bit encoding on the Web, backwards compatible with ASCII
#
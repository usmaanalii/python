# CONTROL STRUCTURES !!
wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)


print(letterlist)

# LIST COMPREHENSION
wordlist = ['cat', 'dog', 'rabbit']
[character for character in "".join(wordlist)]

# REMOVE DUPLICATES (1)
wordlist = ['cat', 'dog', 'rabbit']
singular = []
[singular.append(character) for character in "".join(
    wordlist) if character not in singular]
print(singular)

# REMOVE DUPLICATES (2) (ORDER INCORRECT HOWEVER DUPLICATION REMOVAL WAS A
# SUCCESS)
wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)

singular = list(set(letterlist))
print(singular)

# REMOVE DUPLICATES (3)

set([word[i] for word in ["cat", "dog", "rabbit"] for i in range(len(word))])

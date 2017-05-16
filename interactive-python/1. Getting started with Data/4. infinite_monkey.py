# THE INFINITE MONKEY THEOREM

# 1. write a function that generates a string that is 27 characters long
#    by choosing random letters from the
#    26 letters in the alphabet plus the space
# 2. write a function that will score each generated string
#    by comparing the randomly generated string to the goal
# 3. write a function that repeatedly calls generate and score
#    by checking whether or not the score is 100% you pass or fail the input
#    if there are 1000 fails, print the best scored string along with its score

import string
import random

characters_list = list(string.ascii_lowercase)
characters_list.append(" ")
result_string = 'me thinks it is like a weasel'


def generator():
    test_string_list = []
    for i in range(len(result_string)):
        random_number = random.randint(0, 26)
        test_string_list.append(characters_list[random_number])

    test_string = "".join(test_string_list)
    return test_string


def scorer(test_string, result_string):
    test_score = 0
    for x, y in zip(list(test_string), list(result_string)):
        if x == y:
            test_score += (100 / len(test_string))

    return test_score


def checker():
    dict = {}
    for i in range(1000):
        test_string = generator()
        # returns a string to input as a parameter into the scorer function
        test_score = scorer(test_string, result_string)

        dict[test_string] = test_score

    print(max(dict.items(), key=lambda k: k[1]))


checker()

# THE RESULT WILL BE A DICTIONARY KEY VALUE PAIR, WITH THE STRING TYPED
# AND ITS RELATED 'SIMILARITY SCORE' AS A PERCENTAGE NUMBER

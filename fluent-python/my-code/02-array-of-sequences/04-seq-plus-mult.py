# ** Using + and * with sequences
list_example_3 = [1, 2, 3]
list_example_3 * 5

5 * 'abcd'

# ** Building lists of lists

# Example 2.12 - A list with 3 lists of length 3 can represent Tic-tac-toe
board = [['_'] * 3 for i in range(3)]
board
board[1][2] = 'X'
board

# Example 2.13 - A list with three references to the same list is useless
#   - The same 'row' is appended 3 times
weird_board = [['_'] * 3] * 3
weird_board
weird_board[1][2] = 'O'
weird_board

from board import Board
from knight import Knight

board = Board(3)
blue = Knight('Blue')
red = Knight('red')

print (board)

board.add_knight(blue, 0, 1)
board.add_knight(red, 0, 2)



print (board)
# print(blue.position)
# print(red.position)


matches = next(x for x in board.squares if ...)


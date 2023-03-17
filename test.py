from board import Board
from knight import Knight

board = Board(3)
blue = Knight('Blue')
red = Knight('red')


board.add_element(blue, 0, 1)
board.add_element(red, 0, 2)


print (board)
print(blue.position)
print(red.position)
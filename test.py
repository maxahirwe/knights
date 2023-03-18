from board import Board
from knight import Knight
from item import Item

import numpy as np

board = Board(8)
# grouped = np.array_split(board.squares, 8)

# print(board.squares[0])

blue = Knight('Blue', 'B')
red = Knight('Red', 'R')
green = Knight('Green', 'G')

# knights = [green]

# item = Item('Axe', 'A', 2, 0, 1)

# print(board)
# print(board.get_arr_pos(1, 2))
board.add_knight(green, 0, 0)
# board.add_knight(red, 7, 0)

# board.move()
# board.add_item(item, 1, 2)

# foundKnight = board.find_square_by_knight_symbol('G')['tile']

print(foundKnight.get_coordinates())

# print(board)

board.move('G', 'N')
# board.move(board.get_square(foundKnight.x, foundKnight.y), 'W')
# board.move(board.get_square(foundKnight.x, foundKnight.y), 'W')

# print(board)
print(green.get_coordinates())
# print(red.get_coordinates())

# print(board.output(knights))
# board.output(knights)
# board.move(board.get_arr_pos(foundKnight.x, foundKnight.y), 'W')

# board.add_knight(red, 1, 2)

# print(board.nextMoveCoordinates(1, 1, 'W'))

# print(board)
# print(blue.coordinates)
# print(red.coordinates)

# board.move(board.get_arr_pos(foundKnight.x, foundKnight.y), 'N')
# print(board)

# items = [
#     Item('Axe', 'A', 2, 0, 1),
#     Item('BAxe', 'XAyy', 2, 0, -9),
#     Item('BAxe', 'XA', 2, 0, 0)
# ]

# new_list = sorted(items, key=lambda x: x.ordering)
# print(new_list[0].symbol)

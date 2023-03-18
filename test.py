from board import Board
from knight import Knight
from item import Item

board = Board(3)
blue = Knight('Blue', 'B')
red = Knight('Red', 'R')

item = Item('Axe', 'A', 2, 0, 1)

# print(board)
# print(board.get_arr_pos(1, 2))
board.add_knight(blue, 1, 1)
board.add_item(item, 1, 2)

foundKnight = board.find_knight_by_symbol('B')['tile']

print(foundKnight.getCordinates())

print(board)

board.move(board.get_arr_pos(foundKnight.x, foundKnight.y), 'N')
board.move(board.get_arr_pos(foundKnight.x, foundKnight.y), 'N')

print(board)

print(blue)

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

from board import Board
from knight import Knight
from item import Item

board = Board(8)

knights = [
    Knight('RED', 'R'),
    Knight('BLUE', 'B'),
    Knight('GREEN', 'G'),
    Knight('YELLOW', 'Y')
]

items = [
    {
        'item': Item('Axe', 'A', 2, 0, 1),
        'pos': {
            'x': 2,
            'y': 2
        }
    },
    {
        'item': Item('Dagger', 'D', 1, 0, 3),
        'pos': {
            'x': 2,
            'y': 5
        }
    },
    {
        'item': Item('Helmet', 'H', 0, 1, 4),
        'pos': {
            'x': 5,
            'y': 5
        }
    },
    {
        'item': Item('MagicStaff', 'M', 1, 1, 2),
        'pos': {
            'x': 5,
            'y': 2
        }
    },
]

# for k in knights:
#     board.add_knight(k)

for i in items:
    board.add_item(i['item'], i['pos']['x'], i['pos']['y'])

print(board)

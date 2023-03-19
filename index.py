from board import Board
from knight import Knight
from item import Item
import pprint
import json

board = Board(8)

knights = [{
    'knight': Knight('RED', 'R'),
    'pos': {
        'x': 0,
        'y': 0
    }
}, {
    'knight': Knight('BLUE', 'B'),
    'pos': {
        'x': 7,
        'y': 0
    }
}, {
    'knight': Knight('GREEN', 'G'),
    'pos': {
        'x': 7,
        'y': 7
    }
}, {
    'knight': Knight('YELLOW', 'Y'),
    'pos': {
        'x': 0,
        'y': 7
    }
}]

items = [
    {
        'item': Item('MagicStaff', 'M', 1, 1,
                     2),  # (A, M, D, H) priority order
        'pos': {
            'x': 5,
            'y': 2
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
        'item': Item('Dagger', 'D', 1, 0, 3),
        'pos': {
            'x': 2,
            'y': 5
        }
    },
    {
        'item': Item('Axe', 'A', 2, 0, 1),
        'pos': {
            'x': 2,
            'y': 2
        }
    },
]

for k in knights:
    board.add_knight(k['knight'], k['pos']['x'], k['pos']['y'])

for i in items:
    board.add_item(i['item'], i['pos']['x'], i['pos']['y'])

print('-' * 150)
# add all elements to the board in their rrspective coordinates/positions
all_elements = list(map(lambda x: x['knight'], knights))
all_elements.extend(list(map(lambda x: x['item'], items)))

# apply all movements
filename = 'moves.txt'
lines = open(filename, 'r').read().split('\n')

# print(board)
for line in lines:
    if ':' in line:
        set = line.split(':')
        symbol = set[0].upper()
        direction = set[1].upper()
        if (set != None and symbol != None):
            board.move(symbol, direction)
print('-' * 150)

output = board.output(all_elements)
pprint.pprint(output)
print('-' * 150)

# Writing to final_state.json
json_object = json.dumps(output, indent=2)

with open("./outputs/final_state.json", "w") as outfile:
    outfile.write(json_object)
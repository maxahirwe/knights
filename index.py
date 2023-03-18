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
        'item': Item('MagicStaff', 'M', 1, 1, 2),
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

# add all elemts to the board in their rrspective coordinates/positions
all_elements = list(map(lambda x: x['knight'], knights))
all_elements.extend(list(map(lambda x: x['item'], items)))

# apply all movements
filename = 'moves.txt'
lines = open(filename, 'r').read().split('\n')

print(lines)
for line in lines:
    if ':' in line:
        set = line.split(':')
        color = set[0].upper()
        direction = set[1].upper()
        print(board.find_knight_by_symbol(color))
        square = board.find_knight_by_symbol(color)
        knight = square['tile'] if square != None else None
        if (knight != None):
            board.move(board.get_arr_pos(knight.x, knight.y), direction)
print('-' * 150)

output = board.output(all_elements)
pprint.pprint(output)
print('-' * 150)

# Writing to final_state.json
json_object = json.dumps(output, indent=2)

with open("./outputs/final_state.json", "w") as outfile:
    outfile.write(json_object)
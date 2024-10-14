from string import Template
from collections import OrderedDict
import numpy as np


class Board:

    # initialization of the board based on needed size
    def __init__(self, size):
        self.size = size
        self.square_size = size**2
        self.squares = np.array_split(
            [dict(tile=None, items=[]) for x in range(self.square_size)], 8)

    # get a square based on x,y 2d coordinates
    def get_square(self, x, y):
        if ((x >= self.size or y >= self.size) or (x < 0 or y < 0)):
            return None
        else:
            return self.squares[x][y]

    # add knight to the board at provided coordinates
    def add_knight(self, knight, x_pos, y_pos):
        square = self.get_square(x_pos, y_pos)
        if (square == None):
            raise Exception(
                Template(
                    "knight cannot be placed in given position [$x,$y], $s").
                substitute(x=x_pos, y=y_pos, s=square))
        if (square['tile'] == None):
            knight.change_coordinates(x_pos, y_pos)
            square['tile'] = knight
            print('Added: knight(%s-%s) at (%s, %s)' %
                  (knight.color, knight.symbol, knight.x, knight.y))

        else:
            raise Exception(
                Template("position [$x,$y] already has an knight").substitute(
                    x=x_pos, y=y_pos))

    # sort items on each board square per priority
    def sort_items(self, square):
        square['items'] = sorted(
            square['items'],
            key=lambda x: x.ordering,
        )  #sort by ordering

    # add items to the board at provided coordinates
    def add_item(self, item, x_pos, y_pos):
        square = self.get_square(x_pos, y_pos)
        square['items'].append(item)
        self.sort_items(square)
        item.x = x_pos
        item.y = y_pos
        print('Added: item(%s-%s) at (%s, %s):(Attack:%s , Defend:%s)' %
              (item.name, item.symbol, item.x, item.y, item.attack_points,
               item.defend_points))

    # searches the first square on the board that contains a knight with a given symbol (ex:R OR B)
    def find_square_by_knight_symbol(self, symbol):
        square = None
        for squareGroup in self.squares:
            if (square != None):
                break
            square = next(
                (x for x in squareGroup
                 if x['tile'] != None and x['tile'].symbol == symbol), None)

        return square

    # identifies the next move/square/coordinates based on current x,y coordinates and the direction(N,E,S,W)
    def get_next_move_coordinates(self, x, y, direction):
        new_coordinates = None
        if (direction == 'E'):
            # move east
            new_coordinates = [x, y + 1]
        elif (direction == 'W'):
            # move west
            new_coordinates = [x, y - 1]
        elif (direction == 'N'):
            # move north
            new_coordinates = [x - 1, y]
        elif (direction == 'S'):
            # move south
            new_coordinates = [x + 1, y]
        else:
            raise Exception('Direction must only be one of (N,S,E,W), given',
                            direction)
        new_x = new_coordinates[0]
        new_y = new_coordinates[1]
        res = dict(x=new_x,
                   y=new_y,
                   coordinates=[x, y],
                   dest_square=self.get_square(new_x, new_y),
                   to=[new_x, new_y])
        return res

    # changes a knight's status to DROWNED OR DEAD
    def change_knight_status(self, dest_square, status):
        ACCEPTED_STATUSES = ['DROWNED', 'DEAD']
        if (dest_square['tile'] != None and status in ACCEPTED_STATUSES):
            knight = dest_square['tile']
            item = knight.item
            if (item != None):
                if (status == ACCEPTED_STATUSES[0]):
                    #Knights that drown throw their item to the bank
                    item.equiped = False
                    item.x = knight.x
                    item.y = knight.y
                    dest_square['items'].append(item)
                    self.sort_items(dest_square)

                elif (status == ACCEPTED_STATUSES[1]):
                    #Knights that die in battle drop their item (if they have one)
                    item.equiped = False
                    item.x = None
                    item.y = None
                    dest_square['items'].pop(0)
            dest_square['items'].append(item)  #leave items before drowning
            knight.item = None
            knight.status = status
            knight.change_coordinates(None, None)
            knight.base_attack_score = 0
            knight.base_defend_score = 0
            dest_square['tile'] = None
            print('status change: knight(%s-%s) status(%s), %s)' %
                  (knight.color, knight.symbol, knight.status, knight.item))
        else:
            raise Exception('Unsopported status')

    # moves a knights accross the board
    def move(self, symbol, direction):
        """
        moves a knights accross the board
        symbol: knight symbol, can be one of (R,B,G,Y)
        direction: movement direction, can be one of (N,S,E,W)
        """
        origin_square = self.find_square_by_knight_symbol(symbol)
        if (origin_square != None):
            #knight exists
            knight = origin_square['tile']
            nextMove = self.get_next_move_coordinates(knight.x, knight.y,
                                                      direction)
            dest_square = nextMove['dest_square']
            if (dest_square == None):
                # tile does not exist drowning
                self.change_knight_status(origin_square, 'DROWNED')
            else:
                # tile exist
                dest_items = dest_square['items']
                item = next(iter(dest_items), None)
                #inherit item in given order
                if (knight.item == None and item != None
                        and item.equiped == False):
                    item.equiped = True
                    knight.item = item
                    dest_square['items'].pop(0)
                    print(
                        'earned: knight(%s-%s) item(%s-%s) with (attack:%s-defense:%s) at (%s, %s)'
                        % (knight.color, knight.symbol, item.name, item.symbol,
                           knight.total_attack_score(),
                           knight.total_defend_score(), item.x, item.y))

                #defending knight
                def_knight = dest_square['tile']
                if (def_knight != None):
                    attack_res = knight.attack(def_knight)
                    if (attack_res):
                        # attacker wins, movement
                        self.change_knight_status(dest_square, 'DEAD')
                        origin_square['tile'] = None
                        dest_square['tile'] = knight
                        print(
                            'moved-attacker win: knight(%s-%s) with attack(%s) vs defense(%s)'
                            % (knight.color, knight.symbol,
                               knight.total_attack_score(),
                               def_knight.total_attack_score()))
                        print(
                            'moved(%s): knight(%s-%s) from(%s, %s) => to(%s, %s)'
                            %
                            (direction, knight.color, knight.symbol, knight.x,
                             knight.y, nextMove['x'], nextMove['y']))
                        knight.change_coordinates(nextMove['x'], nextMove['y'])
                    else:
                        # defender win, no movement
                        self.change_knight_status(origin_square, 'DEAD')
                        origin_square['tile'] = None
                        print(
                            'stayed-defender win: knight(%s-%s) with attack(%s) vs defense(%s)'
                            % (knight.color, knight.symbol,
                               knight.total_attack_score(),
                               def_knight.total_defend_score()))
                else:
                    print(
                        'moved(%s): knight(%s-%s) from(%s, %s) => to(%s, %s)' %
                        (direction, knight.color, knight.symbol, knight.x,
                         knight.y, nextMove['x'], nextMove['y']))
                    knight.change_coordinates(nextMove['x'], nextMove['y'])
                    origin_square['tile'] = None
                    dest_square['tile'] = knight

    # output that provides status for all items on board
    def output(self, knights_or_items):
        output = OrderedDict()
        for k in knights_or_items:
            output[k.get_name()] = k.output()

        return output

    def __str__(self):
        output = Template('$size => $square')
        formatted_output = output.substitute(size=self.square_size,
                                             square=self.squares)
        return formatted_output

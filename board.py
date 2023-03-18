from string import Template


class Board:

    def __init__(self, size):
        self.size = size
        self.square_size = size**2
        self.squares = [
            dict(tile=None, items=[]) for x in range(self.square_size)
        ]

    def get_arr_pos(self, x, y):
        if (x >= self.size or y >= self.size):
            return None
        else:
            pos = (y * (y + 1)) + x
            res = pos if pos < self.square_size else None
            return res

    def add_knight(self, knight, x_pos, y_pos):
        position = self.get_arr_pos(x_pos, y_pos)
        if (position == None):
            raise Exception(
                Template(
                    "knight cannot be placed in given position [$x,$y], $s").
                substitute(x=x_pos, y=y_pos, s=position))
        square = self.squares[position]
        if (square['tile'] == None):
            knight.changeCoordinates(x_pos, y_pos)
            square['tile'] = knight
        else:
            raise Exception(
                Template("position [$x,$y] already has an knight").substitute(
                    x=x_pos, y=y_pos))

    def add_item(self, item, x_pos, y_pos):
        position = self.get_arr_pos(x_pos, y_pos)
        square = self.squares[position]
        square['items'].append(item)
        square['items'] = sorted(
            square['items'],
            key=lambda x: x.ordering,
        )
        item.x = x_pos
        item.y = y_pos

    def find_knight_by_symbol(self, symbol):
        return next((x for x in self.squares
                     if x['tile'] != None and x['tile'].symbol == symbol),
                    None)

    def getNextMoveCoordinates(self, x, y, direction):
        new_coordinates = None
        if (direction == 'N'):
            # move up
            new_coordinates = [x, y + 1]
        elif (direction == 'S'):
            # move down
            new_coordinates = [x, y - 1]
        elif (direction == 'E'):
            # move east
            new_coordinates = [x - 1, y]
        elif (direction == 'W'):
            # move west
            new_coordinates = [x + 1, y]
        else:
            raise Exception('Direction must only be one of (N,S,E,W), given',
                            direction)
        x = new_coordinates[0]
        y = new_coordinates[1]
        res = dict(x=x, y=y, coordinates=[x, y], pos=self.get_arr_pos(x, y))
        return res

    def changeKnightStatus(self, target_square, status):
        if (target_square['tile'] != None and status in ['DROWN', 'DEAD']):
            knight = target_square['tile']
            item = knight.item
            if (item != None):
                item.x = knight.x
                item.y = knight.y
            target_square['items'].append(item)  #leave items before drowning
            knight.item = None
            knight.status = status
            knight.changeCoordinates(None, None)
            knight.base_attack_score = 0
            knight.base_defend_score = 0
            target_square['tile'] = None
        else:
            raise Exception('Unsopported status')

    def move(self, knight_current_position, direction):
        origin_square = self.squares[knight_current_position]
        if (origin_square['tile'] != None):
            #knight exists
            knight = origin_square['tile']
            x = knight.x  # horizontal
            y = knight.y  # vertical
            nextMove = self.getNextMoveCoordinates(x, y, direction)
            print('next move', nextMove)
            dest_position = nextMove['pos']
            if (dest_position == None):
                #If a knight moves off the board then they are swept away and drown immediately. Further moves
                #do not apply to DROWNED knights. The final position of a DROWNED knight is null.
                self.changeKnightStatus(origin_square, 'DROWN')
                print('WRONG MOVEMENT, DROWN')
            else:
                print('VALID MOVEMENT')
                #If a Knight moves onto a tile with an item they are immediately equipped with that item, gaining the bonus
                dest_square = self.squares[dest_position]
                dest_items = dest_square['items']
                item = next(iter(dest_items), None)

                #inherit item in given order
                if (knight.item == None and item != None):
                    print('INHERIT ELEMENTS', dest_square['items'], item)
                    print(item)
                    knight.item = item
                    dest_square['items'].pop(0)

                #attack
                dest_defender_knight = dest_square['tile']
                if (dest_defender_knight != None):
                    attack_res = knight.attack(dest_defender_knight)
                    if (attack_res):
                        # attacker win, movement
                        self.changeKnightStatus(dest_square, 'DEAD')
                        origin_square['tile'] = None
                        dest_square['tile'] = knight
                        knight.changeCoordinates(nextMove['x'], nextMove['y'])
                    else:
                        # defender win, no movement
                        self.changeKnightStatus(origin_square, 'DEAD')
                        origin_square['tile'] = None
                else:
                    knight.changeCoordinates(nextMove['x'], nextMove['y'])
                    origin_square['tile'] = None
                    dest_square['tile'] = knight

    def __str__(self):
        output = Template('$size => $square')
        formatted_output = output.substitute(size=self.square_size,
                                             square=self.squares)
        return formatted_output

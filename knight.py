from functools import reduce
from string import Template

KNIGHT_STATUSES = ['LIVE', 'DEAD', 'DROWNED']
DIRECTIONS = ['N', 'E', 'S', 'W']
SUPRISE_ELEMENT_SCORE = 0.5


class Knight:

    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol
        self.base_attack_score = 1  # attack score
        self.base_defend_score = 1  # defend score
        self.status = KNIGHT_STATUSES[0]
        self.item = None  # items that a knight can collect as we progress
        self.x = None
        self.y = None

    # get knight name
    def get_name(self):
        return self.color.lower()

    # get knight's total attack score
    def total_attack_score(self):
        attack_points = self.item.attack_points if self.item != None else 0
        return self.base_attack_score + attack_points

    # get knight's total defend score
    def total_defend_score(self):
        defend_points = self.item.defend_points if self.item != None else 0
        return self.base_defend_score + defend_points

    # perfoms an attack on a defender knight and evalutates the winer/looser, returns boolean
    def attack(self, def_knight):
        attacker_total_points = self.total_attack_score(
        ) + SUPRISE_ELEMENT_SCORE
        defender_total_points = def_knight.total_defend_score()
        print(
            'attack: knight(%s-%s) status(%s) attacking(%s) VS knight(%s-%s) status(%s) defending(%s) happening at att(%s, %s):def(%s, %s)'
            % (self.color, self.symbol, self.status, attacker_total_points,
               def_knight.color, def_knight.symbol, def_knight.status,
               defender_total_points, self.x, self.y, def_knight.x,
               def_knight.y))
        return attacker_total_points > defender_total_points

    # change x,y coordinates
    def change_coordinates(self, x, y):
        self.x = x
        self.y = y
        if (self.item != None):  # change item position as well
            self.item.x = self.x
            self.item.y = self.y

    # get x,y coordinates
    def get_coordinates(self):
        return [self.x, self.y] if self.x != None else None

    # get x,y coordinates in string format
    def get_coordinates_str(self):
        return Template('[$x, $y]').substitute(x=self.x, y=self.y)

    # generate output for console and file extration
    def output(self):
        item_res = self.item.get_name() if self.item else None
        return [
            self.get_coordinates(), self.status, item_res,
            self.total_attack_score(),
            self.total_defend_score()
        ]

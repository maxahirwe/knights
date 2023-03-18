from functools import reduce
from string import Template

KNIGHT_STATUSES = ['ALIVE', 'DEAD', 'DROWNED']
DIRECTIONS = ['N', 'E', 'S', 'W']
SUPRISE_ELEMET_SCORE = 0.5


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
        # self.coordinates = []
        # self.coordinates_str = None

    def total_attack_score(self):
        return self.base_attack_score + self.item.attack_points if self.status == KNIGHT_STATUSES[
            0] else 0

    def total_defend_score(self):
        return self.base_defend_score + self.item.defend_points if self.status == KNIGHT_STATUSES[
            0] else 0

    def attack(self, defender_knight):
        attacker_total_points = self.total_attack_score + SUPRISE_ELEMET_SCORE
        defender_total_points = defender_knight.total_defend_score
        return attacker_total_points > defender_total_points

    def changeCoordinates(self, x, y):
        # coordinates_str = Template('[$x, $y]').substitute(x=x, y=y)
        # self.coordinates = [x, y]
        # self.coordinates_str = coordinates_str
        self.x = x
        self.y = y

    def getCordinates(self):
        return [self.x, self.y]

    def getCoordinatesStr(self):
        return Template('[$x, $y]').substitute(x=self.x, y=self.y)

    def __str__(self):
        return self.getCoordinatesStr()
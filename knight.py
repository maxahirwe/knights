from functools import reduce
from string import Template

KNIGHT_STATUSES = ['LIVE', 'DEAD', 'DROWNED']
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

    def get_name(self):
        return self.color.lower()

    def total_attack_score(self):
        attack_points = self.item.attack_points if self.item != None else 0
        return self.base_attack_score + attack_points if self.status == KNIGHT_STATUSES[
            0] else 0

    def total_defend_score(self):
        defend_points = self.item.defend_points if self.item != None else 0
        return self.base_defend_score + defend_points if self.status == KNIGHT_STATUSES[
            0] else 0

    def attack(self, defender_knight):
        print('defender_knight', defender_knight)
        attacker_total_points = self.total_attack_score(
        ) + SUPRISE_ELEMET_SCORE
        defender_total_points = defender_knight.total_defend_score()
        return attacker_total_points > defender_total_points

    def changeCoordinates(self, x, y):
        self.x = x
        self.y = y

    def get_cordinates(self):
        return [self.x, self.y] if self.x != None else None

    def get_coordinatesStr(self):
        return Template('[$x, $y]').substitute(x=self.x, y=self.y)

    def output(self):
        item_res = self.item.get_name() if self.item else None
        return [
            self.get_cordinates(), self.status, item_res,
            self.base_attack_score, self.base_defend_score
        ]

    # def __str__(self):
    #     return self.getCoordinatesStr()

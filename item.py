from string import Template


class Item:

    def __init__(self, name, symbol, attack_points, defend_points, ordering):
        self.name = name
        self.symbol = symbol
        self.attack_points = attack_points
        self.defend_points = defend_points
        self.ordering = ordering
        self.x = None
        self.y = None

    def getCordinates(self):
        return [self.x, self.y]

    def getCoordinatesStr(self):
        return Template('[$x, $y]').substitute(x=self.x, y=self.y)

    def __str__(self):
        return self.getCoordinatesStr()

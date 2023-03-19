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
        self.equiped = False

    # get item name
    def get_name(self):
        return self.name.lower()

    # get x,y coordinates
    def get_coordinates(self):
        return [self.x, self.y]

    # get x,y coordinates in string format
    def get_coordinates_str(self):
        return Template('[$x, $y]').substitute(x=self.x, y=self.y)

    # generate output for console and file
    def output(self):
        return [self.get_coordinates(), self.equiped]

    def __str__(self):
        return self.get_coordinates_str()

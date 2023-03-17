from functools import reduce

KNIGHT_STATUSES =['ALIVE','DEAD','DROWNED']
DIRECTIONS = ['N','E','S','W']
class Knight:
	def __init__(self, color):
		self.color = color
		self.base_attack_score = 1 # attack score
		self.base_defend_score = 1 # defend score
		self.status = KNIGHT_STATUSES[0]
		self.items = [] # items that a knight can collect as we progress
		self.position = None
		self.position_str = None

	#equip an item to a knight
	def equip(self, item):
		self.items.append(item)
		# build logic to compute scores accordingly

	#def total_attack_score():	
		#base_attack_score + reduce(lambda x, y:x+y, items.map())

	#def total_defend_score():	

	#def attack(self, opponent_knight):

		
	  	


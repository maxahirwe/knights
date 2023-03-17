from string import Template

class Board:
	def __init__(self, size):
		self.size = size
		self.square_size = size  ** 2
		self.squares = [dict(tile=None,item=None) for x in range(self.square_size)]


	def add_knight(self, knight, x_pos, y_pos):
		position = x_pos + 1  * y_pos + 1
		if (position < 0  or position > self.size) :
			raise Exception(Template("knight cannot be placed in given position [$x,$y], $s ").substitute(x=x_pos,y=y_pos, s=position))
		square = self.squares[position]
		if(square['tile'] == None):
			square['tile']  = knight 
			position_str = Template('[$x, $y]').substitute(x=x_pos, y=y_pos)
			knight.position = [x_pos, y_pos]
			knight.position_str = position_str
		else:
			raise Exception(Template("position [$x,$y] already has an knight").substitute(x=x_pos, y=y_pos))

	def add_item(self, item, x_pos, y_pos):
		position = x_pos + 1  * y_pos + 1
		if (position < 0  or position > self.size) :
			raise Exception(Template("element cannot be placed in given position [$x,$y], $s ").substitute(x=x_pos,y=y_pos, s=position))
		square = self.squares[position]
		if(square['item'] == None):
			square['item']  = item 
			pos = Template('[$x, $y]').substitute(x=x_pos, y=y_pos)
		else:
			raise Exception(Template("position [$x,$y] already has an item").substitute(x=x_pos, y=y_pos))		


	def move(self, knight, color, direction):
		# find dict containing knight with that color
		# computer new position
		# move to new position
		current_position = knight.position
		x = new_position[0] # horizontal
		y = new_position[1] # vertical
		new_coordinates = None
		new_position = None

		if(direction == 'N'):
			print('move up')
			new_coordinates = [x, y + 1]
		elif(direction == 'S'):
			print('move down')
			new_coordinates = [x, y - 1]
		if(direction == 'E'):
			print('move east')
			new_coordinates = [x - 1, y]
		if(direction == 'W'):
			print('move west')
			new_coordinates = [x + 1, y]			
		new_position =new_coordinates[0] * new_coordinates[1]

		if (new_position < 0  or new_position > self.size):
		#If a knight moves off the board then they are swept away and drown immediately. Further moves
		#do not apply to DROWNED knights. The final position of a DROWNED knight is null.	
			print('DROWN')
	
		else:
			print('CHANGE POSITION')

	def __str__(self):
		output = Template('$size => $square')
		formatted_output = output.substitute(size= self.size,square=self.squares)
		return formatted_output



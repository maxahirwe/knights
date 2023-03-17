from string import Template

class Board:
	def __init__(self, size):
		self.size = size
		self.square_size = size  ** 2
		self.square = [None] * (self.square_size)

	def add_element(self, element, x_pos, y_pos):
		position = x_pos + 1  * y_pos + 1

		if (position < 0  or position >= self.size) :
			raise Exception(Template("element cannot be placed in given position [$x,$y], $s ").substitute(x=x_pos,y=y_pos, s=position))

		if(self.square[position] == None):
			self.square[position] = element 
			pos = Template('[$x, $y]').substitute(x=x_pos, y=y_pos)
			element.position = pos
		else:
			raise Exception(Template("position [$x,$y] already has an item").substitute(x=x_pos,y=y_pos))

	#def move(element):	

	def __str__(self):
		output = Template('$size => $square')
		formatted_output = output.substitute(size= self.size,square=self.square)
		return formatted_output



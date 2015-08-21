


class Square(object):
	def __init__(self,side):
		self.side = side


	@property
	def area(self):
		return self.side*self.side


	@area.setter
	def area(self,area):
		print('Cant set the area')


test = Square(5)
print(test.area)
test.area = 45
print(test.area)
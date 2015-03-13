

class grish:
	def __init__(self,x,y):
		self.x = x;
		self.y= y;

	def work(self):
		return self.x +self.y


	def __str__(self):
		return "%d %d " % (self.x,self.y)


	def evalualte(self,string):
		return eval(string)
	def __repr__(self):
		return ""



g2 = grish(5,7)
print(g2.evalualte("(4+5)*5/56+(98/2)"))
print(repr(g2))
		


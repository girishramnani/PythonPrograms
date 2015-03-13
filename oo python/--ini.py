class stack(list):
	
	def __init__(self,*args):
		super().__init__(*args)
	def push(self,num):
		self.append(num)
	def pop(self):
		t= self[-1]
		del(self[-1])
		return t
	def __str__(self):
		return super().__str__()
y =stack([1,2,4])

print(y.pop())
print(y.pop())
print(y.pop())
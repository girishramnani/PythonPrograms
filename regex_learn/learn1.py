class person:
	def __init__(self,name,designation,email=None,number=None):
		self.name=name
		self.designation=designation
		self.email =email
		self.number=number
	def __str__(self):
		list =[self.name,self.designation,self.email if self.email else "None",self.number if self.number else "None" ]
		return " ".join(list)

file  = open("name.txt")
data = file.read()
import re
print(data)
names = re.findall(r'\w*,\w*',data) # name

# better number search
numbers= re.findall(r'\d{10}',data)
designation = re.findall(r'\w*-?\w*\n',data)

emails = re.findall(r'\w*@\w*[\.\w*]*',data)
li_names =[]
for i,name in enumerate(names):
	p = person(name,designation[i][:-1],emails[i],numbers[i])
	li_names.append(p)

print(li_names)



# now the tutors method 



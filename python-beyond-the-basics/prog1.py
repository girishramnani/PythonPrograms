__author__ = 'girish'
""" the use and working of map"""


""" creating a wrapper to check the working of the map"""
class Trace :
    def __init__(self):
        self.enable =True
    def __call__(self, f):
        def wrap(*args,**kwargs):

            if self.enable:
                print("Calling {}".format(f))
            return f(*args,**kwargs)
        return wrap
"""this shows the lazy working of map"""

result = map(Trace()(ord),"hello this a a tutorial")
print("hasnt printed anything")
print(result)
print(next(result))


"""well you can also give as many inputs as you like given that the function passed takes in that many parameters"""
result = map(lambda x,y: x+y,[1,2,3],[4,5,6])
for x in result : print(x)
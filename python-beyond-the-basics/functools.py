__author__ = 'girish'
""" this code shows the use and working of filter"""
odd = list(filter(lambda x : x%2!=0,[1,2,3,4,5]))
print(odd)

"""this code explains the use of reduce method"""
import operator

from functools import reduce


multi = reduce(operator.mul,[1,2,3,4,5])
print(multi) #this returns 5! that is 120

""" u can use reduce to get n! in just one line"""
def fact(n):
    return reduce(lambda x,y :x*y,range(1,n+1))
print(fact(5))



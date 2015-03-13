import itertools
import time

def seive():
	nums = itertools.count(2)
	while 1:
		n = next(nums)
		nums = filter(lambda k,n=n: k%n!=0,nums )
		yield n


for i in seive():
	print(i)

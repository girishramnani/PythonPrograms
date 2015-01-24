

for x in range(int(input())):
	input()
	li = [int(x) for x in input().split()]
	t = sum(li)
	t2 = sum([x for x in li if x>0])
	
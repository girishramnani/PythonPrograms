itera = int(input())
l=list()
def fact(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*fact(n-1)
for z in range(itera):
    temp=int(input())
    l.append(fact(temp))

for k in range(itera):
    print(l[k])

    
        

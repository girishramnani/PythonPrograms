import math
sum=0
n=60851475143
i=2

while i <=math.sqrt(n):
    print(i)
    while n%i==0:
        print(i)
        n/=i
    i+=1




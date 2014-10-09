
import math
l=list()

def get2(num):
    count =0
    while(num>1):
        num=int(num/2)
        count+=1
    return count



while(True):
    temp = int(input())
    if (temp == 0):
        break
    else:
        l.append(get2(temp))


for i in range(len(l)):
    print(l[i])
    

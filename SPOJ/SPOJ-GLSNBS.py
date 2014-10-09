
import math

ans_list=[]
while(True):
    num = input().split(" ")
    num = list(map(int,num))
    if num[0] == -1 and num[1] ==-1:
        break
    ans_list.append(math.ceil(max(num[0],num[1])/(min(num[1],num[0])+1)))
print()
for i in range(len(ans_list)):
    print(ans_list[i])
    
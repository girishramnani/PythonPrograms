

def bsearch(num,li,low=0,high=len(li)):
#    print("low : ",low , "high: ", high)
    if low >= high:
        return -1
    
    li = list(li)    
    mid = int((low+high)/2)
    if num == li[mid]:
        return mid
    elif num > li[mid]:
        return bsearch(num,li,mid+1,len(li))
    elif num < li[mid]:
        return bsearch(num,li,low,mid)

ans_list = []
li=input()
li =li.split(" ")
for i in range(len(li)):
    li[i]=int(li[i])

input()
num_list=input()
num_list= num_list.split(" ")
num_list =list(map(int ,num_list))

for i in range(li[1]):
    input()
    temp = int(input())
    ans_list.append(bsearch(temp,num_list))
    

for i in range(len(ans_list)):
    print(ans_list[i])
    print()
def checker(x,y):
    if(x==y or x==(y+2)):
        return True
    return False

def finder(x,y):
    if (checker(x,y)):
        if(x%2==0):
            return x+y
        return x+y-1
    return "No Number"
    
        

it=int(input())
li = list()
ans_li=list()
for i in range(it):
    li = input().split()
    
    ans_li.append(finder(int(li[0]),int(li[1])))


for i in range(it):
    print(ans_li[i])
    

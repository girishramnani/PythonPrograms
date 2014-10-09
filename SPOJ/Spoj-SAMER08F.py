li = list()
def getSumSquare(n):
    su=0
    for i in range(n+1):
        su+=(i*i)
    return su
        
while(True):
    
    i = int(input())
    if(i==0):
        break
    li.append(getSumSquare(i))


for j in range(len(li)):
    print(li[j])
    
    

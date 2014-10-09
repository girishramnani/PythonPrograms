li = list()
def Maxarray(j,i):
    ans = int(len(j)/i) == len(j)/i
    if ans:
        return int(len(j)/i)
    return int(len(j)/i)+1

def convert(array):
    x=zip(*array)
    x=list(x)
    ans=list()
    for k in range(len(x)):
        ans.append("".join(x[k]))
    ans = "".join(ans)
    return ans
   
def rotate(j,i):
    w= Maxarray(j,i)
    l=[]
    for k in range(0,len(j),i):
        l.append(list(j[k:k+i]))
    for z in range(1,len(l),2):
        l[z].reverse()
    return convert(l)  
    
while(True):
    
    itera = int(input())
    if(itera==0):
        break
    
    j = input()
    print(rotate(j,itera))
    
    

    
    

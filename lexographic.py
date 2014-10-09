def display(array):
    temp=1
    out=0
    for i in range(len(array)-1,-1,-1):
        out+=(array[i]*temp)
        temp*=10
    print(out)

def getMinAndExchange(array,z):
    temp=z+1
    min_val = array[z+1]
    for i in range(z+1,len(array)):
        #print(i)
        if (min_val>array[i]):
            if (array[i]>array[z]):
                min_val=array[i]
                temp=i
    
    x=array[temp]
    array[temp]=array[z]
    array[z]=x
    sort(array,z)
    display(array)
    

def sort(array,index):
    windex=index+1
    for i in range(windex,len(array)):
        for  j in range(i,len(array)):
            if(array[i]>array[j]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
                
 
number = str(input())

li = list()
i=(len(number)-2)




for z in range(len(number)):
    li.append(int(number[z]))

print()
display(li)
while(i>-1):
    k=i+1
    if (li[k]>li[i]):
        getMinAndExchange(li,i)
        i=(len(number)-2)
    else:
        i-=1
        
        






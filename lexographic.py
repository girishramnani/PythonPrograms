def display(array):
    
    out=""
    for i in range(len(array)):
        out+=str(array[i])
    return out

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
    return display(array)
    

def sort(array,index):
    windex=index+1
    for i in range(windex,len(array)):
        for  j in range(i,len(array)):
            if(array[i]>array[j]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
                
iteration = int(input()) 
for zz in range(iteration):
 
    number = str(input())
    li = list()
    i=(len(number)-2)
    for z in range(len(number)):
        li.append(number[z])
    boo = True
    #display(li)
    k=i+1
    if (li[k]>li[i]):
        ans =getMinAndExchange(li,i)
        i=(len(number)-2)        
    else:
        boo= False
    
    if boo:
        print(ans)  
    else:
        print("no answer")
            






import random

def partition(plist,index_pivot=0):
    index_pivot=random.randint(0,len(plist)-1)
    pivot=plist[index_pivot]
    
    print(pivot,index_pivot,plist)
    
    if index_pivot!=0:
        swap(plist,0,index_pivot)
    bound=1
    for i in range(1,len(plist)):
        if plist[i]<pivot:
            swap(plist,i,bound)
            bound+=1
            
            
    swap(plist,plist.index(pivot),bound-1)
    print(plist,bound,"pivot= ",pivot )
    return bound-1
            
            

def swap(l,x,y):
    temp=l[x]
    l[x]=l[y]
    l[y]=temp


def Rselect(plist,i):
    
    pivot=partition(plist)
    print("the location of the pivot is ", pivot)
    if i==pivot:
        print("the i and n are equal",plist[pivot-1])
    elif i>pivot:
        Rselect(plist[pivot:],i-pivot)
    elif i<pivot:
        Rselect(plist[:pivot],i)

        


plist=[8,10,4,2]

Rselect(plist,2)

        
    

        

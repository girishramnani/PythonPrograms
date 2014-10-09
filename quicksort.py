

plist=[x for x in range(5,0,-1)]

def partition(plist,index_pivot=0):
    pivot=plist[index_pivot]
    if index_pivot!=0:
        swap(plist,0,index_pivot)
    bound=1
    for i in range(1,len(plist)):
        if plist[i]<pivot:
            swap(plist,i,bound)
            bound+=1
            print(plist,pivot)
            
    swap(plist,index_pivot,bound-1)
    return bound-1
            
            

def swap(l,x,y):
    temp=l[x]
    l[x]=l[y]
    l[y]=temp
    
def qsort(plist):
    if len(plist)<2:
        return plist
    else:
        piv=partition(plist)
        qsort(plist[:piv-1])
        qsort(plist[piv+1:])

qsort(plist)
print(plist)
    


#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     standford algorithm course pset 1
#              question1
#
# Author:      girish
#
# Created:     11-05-2014
# Copyright:   (c) girish 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

count=0
def mergesort(elist,count):
    total=[]
    #print(count)
    low=0
    high=len(elist)
    #print(len(elist))
    if len(elist)<2:
       return elist,count
    mid=int((low+high)/2)
    enlist=[]
    y,count=mergesort(elist[:mid],count)
    z,count=mergesort(elist[mid:high],count)
    i=0
    j=0

    while(i<len(y) and j<len(z)):
        if y[i]<=z[j]:
           enlist.append(y[i])
           i+=1

        else:
             count+=abs((len(y))-i)
             enlist.append(z[j])
             j+=1

    enlist+=y[i:];
    enlist+=z[j:]

    return enlist,count


for i in range(int(input())):
    input()
    
    li=[int(input()) for k in range(int(input()))]

    x,y=mergesort(li,0)

    print(y)




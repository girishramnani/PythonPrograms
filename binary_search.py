
def insertionSort(li):
    l = len(li)
    for i in range(l):
        temp=li[i]
        j=i
        while li[j]<li[j-1] and j>=0:
            li[j]=li[j-1]
            j-=1
        li[j]=temp
        print(li)
i1 = int(input()) 
li = [int(x) for x in input().split()]
insertionSort(li)           
            
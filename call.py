import random

def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      
 
 
def partition( aList, first, last ) :
    pivot = first + random.randrange( last - first + 1 )
    swap( aList, pivot, last )
    for i in range( first, last ):
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
 
    swap( aList, first, last )
    print(aList,aList[pivot])
    return first
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

alist=[4,3,2,6,2,8,45,32]

quicksort(alist)
#print(alist)

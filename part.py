def qsort(list):
    if len(list)<=1:
        return list
    else:
        return qsort([x for x in list[1:] if x<list[0]]) + [list[0]] + qsort([x for x in list[1:0] if x>=list[0]])


list=[x for x in range(60,6,-2)]
#print(list)
print(qsort(list))


##def qsort(arr): 
##     if len(arr) <= 1:
##          return arr
##     else:
##          return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(greater) + equal + sort(greater) # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print(sort())

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      girish ramnani
#
# Created:     09-04-2014
# Copyright:   (c) girish ramnani 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
'''simple search'''
def search(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
        return False

def bisearch(L,e):
    def bsearch(L,e,low,high):
        if low==high:
            return L[low]==e
        else:
            mid=low +int((low+high)/2)
        if L[mid]==e:
            return True
        if L[mid]>e:
            return bsearch(L,e,low,mid)
        else:
            return bsearch(L,e,mid,high)
    if len(L)==0:
        return False
    else:
        return bsearch(L,e,0,len(L)-1)

print(bisearch([1,2,54,787,67897,5674565756,346456347567575],787))
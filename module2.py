#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      girish ramnani
#
# Created:     02-04-2014
# Copyright:   (c) girish ramnani 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def isPrime2(n):
    if n<2: return False
    if n==2: return True
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True

def fermet(n):
    d=2
    num=((2**(2**n))+1)
    while d<num:

        if(num%d==0):
            print(num%d,d)
            if isPrime2(d):
                print d
                break
        '''while num%d==0:
            if isPrime2(d):
                print d

            num/=d'''
        if num<0:
            break
        d+=1
    print(num)

fermet(7)


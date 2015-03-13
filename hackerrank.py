#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      girish ramnani
#
# Created:     05-04-2014
# Copyright:   (c) girish ramnani 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string

def main():
    pass

if __name__ == '__main__':
    main()
lister=[]
x=raw_input()
for w in range(int(x)):

    i=raw_input()

    boller=0
    v=0
    if i[0]!='_' and i[0]!='.':

        boller=1

    try:
        if int(i[1]) not in range(10):
            print(i[1])
            boller=1
            break
    except ValueError,e:
        boller=1
        break
    finally:
        for j in i[2:]:

            if j in string.ascii_letters:
                v= i.index(j)
                break
        if(v!=0):
            for j in i[v:]:
                if j not in string.ascii_letters:
                    boller=1
                    break

        lister.append(boller)



for boller in lister:
            if(boller):
                print('INVALID')
            else:
                print('VALID')













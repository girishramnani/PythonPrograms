import math

def multi(a,b,call=1):
    if call==0 or (a== 0 or b==0):
        return a*b
    dig10=int(max(math.log10(abs(a))+1,math.log10(abs(b))+1)/2)
    dig=10**dig10
    x1=int(a/(dig))
    x2=a%(dig)
    y1=int(b/(dig))
    y2=b%(dig)

    z1=multi(x1,y1,0)
    z2=multi(x2,y2,0)
    z3=multi(x1+x2,y1+y2,0)-z1-z2
    print (multi(z1,dig**2,0)+multi(z3,dig,0)+z2)



    
    

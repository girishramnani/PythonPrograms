def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


#print(gcd(10,4))

def lcm(a,b,func=gcd):
    gcdn=gcd(a,b)
    lcmn=(a*b)/gcdn
    return lcmn


def lcm_range(last):
    lcmn=2
    first=3
    for i in range(first,last+1):
        lcmn=lcm(lcmn,i)
        print("lcm till ",i, " is ",lcmn)
        for x in range(2,i):
            if lcmn%x!=0:
                print("not zero for ",x)
                
lcm_range(45)

    


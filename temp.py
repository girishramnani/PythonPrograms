import math

    
i = int(input())

if i<=1:
    print("TAK")
elif float(math.log2(i)).is_integer() :
    print("TAK")
else:
    print("NIE")
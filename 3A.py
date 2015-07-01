w1=list(input())
w2=list(input())

import math
motion ={(1,-1):"RD",(-1,-1):"LD",(1,1):"RU",(-1,1):"LU"}


horizontal = ord(w2[0]) - ord(w1[0])
vertical = int(w2[1]) - int(w1[1])
first_move = min(abs(horizontal),abs(vertical))
signs = (math.copysign(1,horizontal),math.copysign(1,vertical))
complex_move = motion[signs]
anslist = []
for i in range(first_move):
    anslist.append(complex_move)

horizontal =signs[0]*(abs(horizontal)-first_move)
vertical =signs[1]*(abs(vertical)-first_move)
horizontal = int(horizontal)
vertical = int(vertical)

if any((horizontal,vertical)):
    if horizontal:
        if horizontal > 0:
            anslist.extend(["R"]*horizontal)
        else:
            anslist.extend(["L"]*abs(horizontal))
    else:
        if vertical > 0:
            anslist.extend(["U"]*vertical)
        else:
            anslist.extend(["D"]*abs(vertical))
print(len(anslist))
for i in anslist:
    print(i)
    

li =list(range(1,41))
import random

for i in range(39):
    A = random.choice(li)
    li.remove(A)
    B = random.choice(li)
    li.remove(B)
    print(li,A,B)
    adding = A+B-1
    li.append(adding)
print(li)

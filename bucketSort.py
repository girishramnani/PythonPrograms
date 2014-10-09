iteration = int(input())
numList =[0]*1000000
for i in range(iteration):
    temp = int(input())
    numList[temp] = 1


for z in range(len(numList)):
    if numList[z] == 1:
        print(z)


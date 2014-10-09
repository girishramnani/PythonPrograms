import random


def FermatPrimalityTest(number):
    if (number > 1):
        for time in range(10): 
            randomNumber = random.randint(2, number)-1
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
            
        return True
    else:
        return False 

ans_list = []     
iteration =int(input())
for i in range(iteration):
    temp =input().split(" ")
    temp=list(map(int,temp))
    for j in range(len(temp)):
        temp[j] = int(temp[j])
        
    for k in range(temp[0],temp[1]+1):
        if FermatPrimalityTest(k):
            ans_list.append(k)
    ans_list.append(' ')

for t in range(len(ans_list)):
    print(ans_list[t])
        


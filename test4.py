li= [ [int(x) for x in input().split() ] for i in range(int(input()))]
li = sorted(li,key=lambda item: item[0])
mi = li[0]
if len(li)==1:
    print("Poor Alex")
else:
    
    for i in range(1,len(li)):
        if li[i-1][1] >li[i][1] :
            print("Happy Alex")
            break
    else:
        print("Poor Alex")
    

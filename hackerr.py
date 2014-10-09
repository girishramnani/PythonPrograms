

i= int(input())
li=[0]*i
ans=[0]*i
loc =0;
for j in range(i):
    li[j]=int(input())
for te in range(i):
    loc+=1
    temp = str(li[te])
    for j in range(len(temp)):
        t = int(temp[j])
        if(t==0):
            continue
        if li[te]%t==0:
            ans[te]+=1

for i in ans:
    print(i)



    

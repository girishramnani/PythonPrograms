filename="input01.txt"
file=open(filename,'r')
li=[]
for i in file:
    i.split()
    li.append(i)

iteration=int(li[0])
gems=li[1]
li=li[2:]
iteration=int(input())


max_i=len(li)
count=0

for char in gems:
    for i in li:
    
        flag=True
        
        if char not in i:
            flag=False
            break
        #print("Flag=",flag," i=",i," char=",char)
    if flag==True:
        count+=1
            
                
print(int(count))   
    
    

    

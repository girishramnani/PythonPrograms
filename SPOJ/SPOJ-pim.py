




ans_list = []
while(True):
    side_street=[]
    no_i = int(input())
    if no_i == 0:
        break
    ans_li = input().split(" ")
    ans_li=list(map(int,ans_li))
    bol="yes"
    j=0
    i=1
    while(len(side_street)>0 or j<no_i):
        
        
        
        if(j<no_i and ans_li[j]==i):
            i+=1
            j+=1
        
        elif(len(side_street)>0 and side_street[-1] == i):
            side_street.pop()
            i+=1
            
        elif(j<no_i):
            side_street.append(ans_li[j])
            j+=1
        else:
            bol="no"
            break
    
    ans_list.append(bol)
    
for i in range(len(ans_list)):
    print(ans_list[i])
            
        
        
 

          
        
            
            
    
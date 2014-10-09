

def appendsums(plist):
    for i in range(26):
        partlist=plist[-1:-4:-1]
        x = sum(partlist)
        plist.append(x)
    return plist

        
        
    


sum_three = [0, 1, 2]
appendsums(sum_three)
print (sum_three[20])

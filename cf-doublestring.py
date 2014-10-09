memory = [-1]*1000
def minsteps(num):
    global memory
    if num==1: return 0
    if memory[num]!=-1:
        return memory[num]
    r = 1+minsteps(num-1)
    if (num%2==0): r = min(r , 1+ minsteps(int(num/2)))
    if (num %3 ==0): r = min(r, 1+minsteps(int(num/3))) 
    memory[num]=r
    return r
    
print(minsteps(10))
    
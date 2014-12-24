# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 16:43:22 2014

@author: girish
"""
magic =[0]
used=[]
board=[]
def initial(n):
    board.extend([[0 for x in range(n)] for y in range(n)])
    used.extend([False for a in range(n**2+1) ])
    magic[0]=n*(n*n+1)//2
def output():
    for row in board:
        for val in row:
            print(val,end=" ")
        print()
        
def isValid(n):
    
    sumD=sumD2=0
    for i in range(n):
        sumv=sumh=0
        sumD+=board[i][i]
        sumD2+=board[i][n-i-1]
        for j in range(n):
            sumv+=board[j][i]
            sumh+=board[i][j]
        if sumv !=magic[0] or sumh !=magic[0]:
            return False
    return sumD==magic[0] and sumD2==magic[0]
def solve(n,step=0):
    if step ==n**2:
        return isValid(n)
    for i in range(1,n*n+1):
        if not used[i]:
            used[i]=True 
            board[step//n][step%n]=i
            if solve(n,step+1):
                return True
            board[step//n][step%n]=0
            used[i]=False
    print(board)
    return False
initial(3)
print(magic)
solve(3)
print(board)


        

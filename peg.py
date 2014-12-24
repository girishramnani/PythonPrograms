# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 15:56:21 2014

@author: girish
"""

def initial(n,skip):
    '''Construct  triangle solitaire game '''
    board={}
    for c in range(0,2*n,2):
        d=0
        for r in range((2*n-c)//2):
            board[(c+d,r)]=True
            d+=1
    if skip in board:
        board[skip]=False
    return board
def solve(board,path):
    ''' Solves board'''
    if len(path)==len(board)-2 :
        return True
    for move in moves(board):
        path.append(move)
        makeMove(board,move)
        
        if solve(board,path):
            return True
        undoMove(board,move)
        del(path[-1])
    return False
directions = [[+4,0],[-4,0],[+2,+2],[+2,-2],[-2,+2],[-2,-2]]
def moves(board):
    '''returns a move'''
    m=[]
    for hole in board:
        if board[hole]:
            for 
    
    
            
            
    
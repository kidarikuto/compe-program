# import my_func
import math 
import sys
import itertools
import bisect
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import deque

if __name__ == '__main__':
    N,Q=map(int,input().split())
    A=deque(map(int,input().split()))
    # T=list(list(map(int,input().split())) for _ in range(Q))
    # print(T)
    # A=deque(A)
    for i in range(Q):
        t,x,y=map(int,input().split())
        if t==1:
            x,y =x-1,y-1
            A[x],A[y]=A[y],A[x]
        elif t==2:
            A.rotate(1)
        elif t==3:
            print(A[x-1])
        # print("A:",*A)


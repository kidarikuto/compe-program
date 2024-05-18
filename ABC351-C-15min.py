# import my_func
import math 
import sys
import itertools
import bisect
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
from collections import deque


if __name__ == '__main__':
    N=int(input())
    A=deque(map(int,input().split()))
    B=[]
    B.append(A[0])
    for i in range(1,N):
        if A[i]==B[-1]:
            B.pop()
            B.append(A[i]+1)
            while len(B)>=2:
                if B[-1]==B[-2]:
                    B.pop()
                    b=B.pop()
                    B.append(b+1)
                else:break
        else:
            B.append(A[i])
    print(len(B))

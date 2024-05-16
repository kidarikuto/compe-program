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
    N,K,P=map(int,input().split())
    A=list(map(int,input().split()))
    # print(A)
    al=A[:N//2]
    ar=A[N//2:]
    # print(al,ar)
    # combl=combinations(al,K//2)
    # combr=combinations(ar,K//2)
    ans=0
    ansl=[]
    ansr=[]
    for i in range(K+1):
        combl=combinations(al,i)
        combr=combinations(ar,i)
        tmp=[]
        for c in combl:
            tmp.append(sum(c))
        ansl.append(tmp)
        tmp=[]
        for c in combr:
            tmp.append(sum(c))
        ansr.append(tmp)
    print(ansl)
    print(ansr)

    for i in range(K+1):
        for l in ansl[i]:
            for r in ansr[-1*(i+1)]:
                if l+r<=P:
                    ans+=1
    print(ans)

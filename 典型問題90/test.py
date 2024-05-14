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
    N=input()
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    # print(A)
    A=[x%46 for x in A]
    A.sort()
    B=[x%46 for x in B]
    B.sort()
    C=[x%46 for x in C]
    C.sort()
    cnt=0
    for x in range(46):
        for y in range(46):
            for z in range(46):
                if (x+y+z)%46==0:
                    xnum=A.count(x)
                    ynum=B.count(y)
                    znum=C.count(z)
                    cnt+=xnum*ynum*znum
    print(cnt)

            
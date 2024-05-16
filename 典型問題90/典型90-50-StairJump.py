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
    N,L=map(int,input().split())
    roop=int(N/L)+1
    ans=0
    for i in range(roop):
        if N - i * L >= 0:  
            tmp=math.comb(N-i*(L-1),i)
            ans+=tmp
        # print(tmp)
    print(ans%(10**9+7))

    
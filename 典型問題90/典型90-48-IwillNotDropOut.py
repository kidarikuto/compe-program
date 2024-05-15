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
    N,K=map(int,input().split())
    allocation=list(list(map(int,input().split())) for _ in range(N))
    # print(allocation)
    allocation.sort(key=lambda x: x[1],reverse=True)
    # print(allocation)
    second=[]
    for i in range(N):
        allocation[i][0] = allocation[i][0]-allocation[i][1]
        second.append(allocation[i][0])
        second.append(allocation[i][1])
    # print(second)
    second.sort(reverse=True)
    # print(second)

    ans=0
    for i in second:
        ans+=i
        K-=1
        if K<=0:
            break
    
    print(ans)
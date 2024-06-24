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
# import numpy as np
import queue

def dfs_template(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # 訪問したノードの処理

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_template(graph, neighbor, visited)

##ABC342-C-TLE
if __name__ == '__main__':
    n=int(input())
    w=list(map(int,input().split()))
    # dp=[[0 for i in range(n)] for j in range(n)] 
    def solve(l,r):
        if r-l<=0:
            return 0
        if r-l==1 and abs(w[r]-w[l])<=1:
            # dp[l][r]=2
            # print(l,r,dp[l][r])
            return 2
        elif r-l==1 and abs(w[r]-w[l])>1:
            # dp[l][r]=0
            # print(l,r,dp[l][r])
            return 0
        elif r-l>=2 and abs(w[r]-w[l])<=1 and solve(l+1,r-1)==r-l-1:
            # dp[l][r]=r-(l-1)
            # print(l,r,dp[l][r])
            return r-(l-1)
        else:
            ret=0
            for i in range(l,r):
                ret=max(ret,solve(l,i)+solve(i+1,r))
            # dp[l][r]=ret
            # print(l,r,dp[l][r])
            return ret
    print(solve(0,n-1)) 
    # print(dp)
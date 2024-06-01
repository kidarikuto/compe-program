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

def dfs_template(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # 訪問したノードの処理

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_template(graph, neighbor, visited)

if __name__ == '__main__':
    n,w=map(int,input().split())
    a=list(list(map(int,input().split())) for i in range(n))
    # print(n,w,a)
    dpv=[[0 for i in range(w+1)] for j in range(n)]
    # dpw=[[w for i in range(w+1)] for j in range(n)]

    for i in range(n):
        for j in range(1,w+1):
            if i==0 and a[i][1]>j:
                pass
            elif i==0 and a[0][1]<=j:
                dpv[0][j]=a[0][0]
            elif i>0 and a[i][1]>j:
                dpv[i][j]=dpv[i-1][j]
            elif i>0 and a[i][1]<=j:
                dpv[i][j]=max(dpv[i-1][j], dpv[i-1][j-a[i][1]] + a[i][0])
        # print(dpv[i])
    print(dpv[n-1][w])

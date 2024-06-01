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
    s=input()
    t="chokudai"
    stack=[[0 for i in range(8)] for j in range(len(s))]
    for i in range(len(s)):
        for j in range(8):
            # print(s[i],t[j])
            if i==0 and s[i]==t[0]:
                stack[i][0]=1
            elif i>0 and j==0 and s[i]==t[j]:
                stack[i][j]=stack[i-1][j]+1
            elif i>0 and j>0 and s[i]==t[j]:
                stack[i][j]=stack[i][j-1]+stack[i-1][j]
            else:
                stack[i][j]=stack[i-1][j]

        # print(stack[i])
    print(stack[len(s)-1][7]%(10**9+7))

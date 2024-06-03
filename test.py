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
import numpy as np

def dfs_template(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # 訪問したノードの処理

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_template(graph, neighbor, visited)

if __name__ == '__main__':
    n=int(input())
    s=input()
    ans=list(s)
    q=int(input())
    dic={}
    for i in range(n):
        if s[i] not in dic:
            dic[s[i]]=[i]
        else:
            dic[s[i]].append(i)
    # print(dic)
    for i in range(q):
        c,d=input().split()
        if c in dic and d in dic:
            if c==d:
                continue
            while len(dic[c])>0:
                t=dic[c].pop()
                ans[t]=d
                dic[d].append(t)
        elif c in dic and d not in dic:
            t=dic[c].pop()
            dic[d]=[t]
            ans[t]=d
            while len(dic[c])>0:
                t=dic[c].pop()
                dic[d].append(t)
                ans[t]=d
        else:
            continue
    print("".join(ans))


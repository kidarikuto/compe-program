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
    n,m,k=map(int,input().split())
    # c=list(list(input().split()) for i in range(m))
    graph=[]
    for i in range(m):
        c=list(input().split())
        a=[c[-1]]
        b=[int(x) for x in c[1:-1]]
        graph.append(a+b)
        # print(c)
    # print(graph)
    numbers = list(range(1, n + 1))

    ans=0
    # すべての組み合わせを生成
    for r in range(0, n + 1):
        combinations = itertools.combinations(numbers, r)
        for combo in combinations:
            # print(combo)
            flag=1
            for i in range(m):
                cnt=0
                for j in graph[i]:
                    if j in combo:
                        cnt+=1
                if graph[i][0]=='o':
                    if cnt<k:
                        flag=0
                        break
                elif graph[i][0]=='x':
                    if cnt>=k:
                        flag=0
                        break
                
            if flag==1:
                ans+=1
    print(ans)


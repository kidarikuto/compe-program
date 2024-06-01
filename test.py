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
    n,m=map(int,input().split())
    mod=998244353
    sum=0
    m_binary=bin(m)[2:]
    m_one_count=m_binary.count("1")
    # print("m_one_count",m_one_count)
    if n==0 or m==0 or n<m:
        print(sum%mod)
        exit()
    sum=m_one_count*2**(int(math.log(n,2))-1)
    # print("sum",sum)
    if m==0:
        print(sum%mod)
        exit()
    start=2**(int(math.log(m,2))+1)+1
    # print("start",start)


    for i in range(start,n+1):
        binary=bin(i&m)[2:]
        # print(binary)
        one_count=binary.count("1")
        # print("one_count",one_count)
        sum+=one_count
    # ans=0
    print(sum%mod)
 
        
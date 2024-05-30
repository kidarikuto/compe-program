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
    S=input()
    n=len(S)
    sorted_string=list(S)
    sorted_string.sort()
    # print(sorted_string)
    ans=0
    seen={}
    set_string=set(sorted_string)
    for i in range(n):
        if S[i] in seen:
            seen[S[i]]+=1
        else:
            seen[S[i]]=1
    # print(set_string)
    cnt=[]
    for i in (set_string):
        # print(set_string[i])
        cnt.append(seen[i]**2)
    # print(cnt)
    sum=sum(cnt)
    print((n**2 - sum)//2)




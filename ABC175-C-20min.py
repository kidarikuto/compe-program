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
    x,k,d=map(int,input().split())
    if abs(x)<=d:
        if k%2==0:
            print(abs(x))
        elif k%2==1:
            print(d-abs(x))
    elif d<abs(x) and abs(x)<=d*k:
        r=abs(x)//d
        k-=r
        if k%2==0:
            print(abs(x)-d*r)
        elif k%2==1:
            print((r+1)*d-abs(x))
    elif d*k<abs(x):
        print(abs(x)-d*k)
        



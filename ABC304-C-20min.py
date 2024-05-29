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
    N,D=map(int,input().split())
    human=list(list(map(int,input().split())) for i in range(N))
    # print(human)
    j=["No" for i in range(N)]
    j[0]="Yes"
    # human.pop(0)
    stack=[0]#新しく感染したときhumanから取り除いてstackに入れる
    while len(stack)>0:
        virus=stack.pop()
        for i in range(N):
            x=(human[virus][0]-human[i][0])**2
            y=(human[virus][1]-human[i][1])**2
            if x+y<=D**2 and j[i]=="No":
                stack.append(i)
                j[i]="Yes"
                # print(i,j)
    for i in range(N):
        print(j[i])

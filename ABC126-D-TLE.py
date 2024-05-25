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
 
def find_list(graph,element):
    ans=[]
    for i in range(len(graph)):
        if element in graph[i]:
            ans.append(graph[i])
    return ans

def abc126_b_dfs(a):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    const_a=find_list(graph,a)#[a,aa,edge]

    for const in const_a:
        a_index=const.index(a)
        aa=const[abs(a_index-1)]
        na=a-1
        naa=aa-1
        if const[2]%2==0:
            visited[naa]=visited[na]
        else:
            visited[naa]=abs(visited[na]-1)
        #visitedに書き込んだ制約を削除したい
        graph.remove(const)
        # print(a,aa)
        # print(visited)
        abc126_b_dfs(aa)


if __name__ == '__main__':
    N=int(input())
    graph=list(list(map(int,input().split())) for i in range(N-1))#編の制約０：ノード1つ目　１：ノード2つ目　２：辺の距離
    # print(graph)
    visited=[-1 for i in range(N)]#１：黒　０：白　ー１：未塗
    flag=1
    
    constraints=graph.pop()
    a=constraints[0]
    na=a-1
    b=constraints[1]
    nb=b-1
    edge=constraints[2]

    visited[na]=0
    if edge%2==0:
         visited[nb]=0
    else:
         visited[nb]=1
    # print(a,b,edge)
    # print(find_list(graph,a))
    # print(find_list(graph,b))
    # print(visited)
    abc126_b_dfs(a)
    abc126_b_dfs(b)

    for a in visited:
        print(a)
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
    N,T=map(int,input().split())
    A=list(map(int,input().split()))
    # print(A)
    flag=0
    cnt=[[0 for i in range(N)],[0 for j in range(N)],0,0]#縦、横、斜め左から、斜め
    for i in range(T):
        # print(A[i])
        x=(A[i]-1)%N
        cnt[0][x]+=1
        y=int((A[i]-1)//N)
        # print("y",y)
        cnt[1][y]+=1
        if x==y:
            cnt[2]+=1
        if x+y==(N-1):
            cnt[3]+=1
        if (N in cnt[0]) or (N in cnt[1]) or (N==cnt[2]) or (N==cnt[3]):
            print(i+1)
            flag=1
            break
        # print(cnt)

    if flag==0:
        print(-1)
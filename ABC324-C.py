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
    N,T=(input().split())
    N=int(N)
    ans=[]
    for i in range(N):
        s=input()
        if len(s)<len(T)-1 or len(T)+1<len(s):
            continue
        flag=0
        cnt=0
        # print(len(s),len(T))
        if len(s)==len(T):#
            for j in range(len(s)):
                # print(s[j],T[j])
                if flag==0 and s[j]==T[j]:
                    continue
                elif flag==0 and s[j]!=T[j]:
                    flag=1
                elif flag==1 and s[j]==T[j]:
                    continue
                elif flag==1 and s[j]!=T[j]:
                    flag=2
                    break
            if flag<2:
                ans.append(i+1)
        if len(s)==len(T)-1:#sのほうが短い
            for j in range(len(T)):
                if flag==0 and cnt==len(s):
                    continue
                if flag==0 and s[cnt]==T[j]:
                    cnt+=1
                elif flag==0 and s[cnt]!=T[j]:
                    flag=1
                
                elif flag==1 and s[cnt]==T[j]:
                    cnt+=1
                elif flag==1 and s[cnt]!=T[j]:
                    flag=2
                    break
            if flag<2:
                ans.append(i+1)

        elif len(s)-1==len(T):#sのほうが長い
            for j in range(len(s)):
                if flag==0 and cnt==len(T):
                    continue
                if flag==0 and T[cnt]==s[j]:
                    cnt+=1
                elif flag==0 and T[cnt]!=s[j]:
                    flag=1
            
                elif flag==1 and T[cnt]==s[j]:
                    cnt+=1
                elif flag==1 and T[cnt]!=s[j]:
                    flag=2
                    break
            if flag<2:
                ans.append(i+1)
    print(len(ans))
    print(*ans)




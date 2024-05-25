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
 
def glid_dfs(h, w):
        visited[h][w] = "o"
        # 四方向を探索
        for dir in range(4):
            nh = h + dy[dir]
            nw = w + dx[dir]
            # 場外アウトしたり、移動先が壁の場合はスルー
            if nh < 0 or nh >= 10 or nw < 0 or nw >= 10:continue
            if graph[nh][nw] == 'x':continue
            # 移動先が探索済みの場合
            if visited[nh][nw]=="o":continue
            # 再帰的に探索
            # if visited[nh][nw]==".":
            glid_dfs(nh,nw)



if __name__ == '__main__':
    # 入力受け取り
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    graph=list(list(input()) for _ in range(10))
    
    flag=0
    
    for i in range(10):
        for j in range(10):
            if graph[i][j]=="x":        
                graph[i][j]="o"
                visited=[["x" for i in range(10)] for j in range(10)]
                glid_dfs(i,j)
                # print(i,j)
                # for a in range(10):
                    # print(graph[i])
                    # print(visited[a])
                if visited==graph:
                    flag=1
                graph[i][j]="x"
                
    if flag==1:
        print("YES")
    else:
        print("NO")
                       
              
    # print(map)
    
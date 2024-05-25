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
 
def dfs(h, w):
        visited[h][w] = 1
        # # print(h,w)
        # for i in range(H):
        #     print(*visited[i])
        # print(visited)
        # 四方向を探索
        for dir in range(4):
            nh = h + dy[dir]
            nw = w + dx[dir]
            # 場外アウトしたり、移動先が壁の場合はスルー
            if nh < 0 or nh >= H or nw < 0 or nw >= W:continue
            if graph[nh][nw] == '#':continue
            # 移動先が探索済みの場合
            if visited[nh][nw]==1:continue
            # 再帰的に探索
            # if visited[nh][nw]==".":
            dfs(nh,nw)
        

if __name__ == '__main__':
    # 四方向への移動ベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    

    # 入力受け取り
    H, W = map(int, input().split())
    # field = [input().strip() for _ in range(H)]
    graph=[]
    for i in range(H):
        t=list(input())
        graph.append(t)
    for h in range(H):# s と g のマスを特定する
        for w in range(W):
            if graph[h][w] == 's':
                sh, sw = h, w
            if graph[h][w] == 'g':
                gh, gw = h, w
    
    # print(sh,sw,gh,gw)
    # visited 配列を0に初期化
    visited = [[0 for i in range(W)] for j in range(H)]
    # print(visited)
    dfs(sh, sw)
    if visited[gh][gw]==1:
        print("Yes")
    else:
        print("No")

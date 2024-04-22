#自作関数のインポート
#import my_func
import math
from itertools import permutations


#point
# 制約が緩いなら順列を全探索しても大丈夫
if __name__ == '__main__':
    N = int(input())
    A = [[]]
    for i in range(N):
        a = [0]
        b = list(map(int,input().split()))
        a += b
        A.append(a)
    # print(A)
    M = int(input())
    uwasa = [[0 for j in range(N+1)] for i in range(N+1)]
    for i in range(M):
        x,y = map(int,input().split())
        uwasa[x][y] = 1
        uwasa[y][x] = 1
    # print(uwasa)
    
    ans = 100000
    perm = list(permutations(range(1, N+1)))
    for p in perm:
        flag = True
        tmp = A[p[0]][1]
        # print(p)
        for i in range(1,len(p)):
            # print(uwasa[p[i-1]][p[i]])
            if uwasa[p[i-1]][p[i]] == 1:
                flag = False
            tmp += A[p[i]][i+1]

        if ans > tmp and flag == True:
            ans = tmp
    if ans == 100000:
        print(-1)
    else:
        print(ans)
        
        

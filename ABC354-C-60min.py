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


if __name__ == '__main__':
    N=int(input())
    a=list(list(map(int,input().split()))for i in range(N))
    ans=[]
    sort=sorted(a,key=lambda x:x[0],reverse=True)
    index_map={element[0]: idx for idx, element in enumerate(a)}
    # print(a)
    # print(sort)
    # print(index_map)
    minc=sort[0]
    ans.append(index_map[sort[0][0]]+1)
    for i in range(N):
        if minc[1]>sort[i][1]:
            ans.append(index_map[sort[i][0]]+1)
            minc=sort[i]
            # print(ans)
    ans.sort()
    print(len(ans))
    print(*ans)

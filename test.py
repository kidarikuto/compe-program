# import my_func
import math 
import sys
import itertools
import bisect
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

if __name__ == '__main__':
    N=int(input()) 
    A=list(map(int,input().split()))   
    ans=0
    start=0
    max_move=0
    move=0
    for i in range(N):
        move+=A[i]
        max_move=max(move,max_move)
        ans=max(ans,start+max_move)
        # print("max_move",max_move,"start",start,"ans",ans)
        start+=move
    print(ans)
        
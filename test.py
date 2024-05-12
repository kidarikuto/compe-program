# import my_func
import math 
import sys
import itertools
import bisect
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

if __name__ == '__main__':
    N=input()
    n=[int(c) for c in N]
    # print(n)
    digi=len(N)
    ans=float("inf")
    for i in range(1,1<<digi):
        sum=0
        cnt=0
        for j in range(digi):
            if i & (1<<j):
                sum+=n[j]
                cnt+=1
        if sum%3==0:
            del_num=digi-cnt
            # print(del_num,sum,i)
            ans=min(ans,del_num)
    if ans==float("inf"):
        print(-1)
    else:
        print(ans)


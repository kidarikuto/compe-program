# import my_func
import math 
import sys
import itertools
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def val_cal(num):
    c=str(num)
    digit=len(c)
    return A*num+B*digit
if __name__ == '__main__':
    N=int(input())
    L=list(map(int,input().split()))
    L.sort()
    # print(L)
    ans=0
    for a in range(N-2):
        cnt=0
        triangle=[]
        for b in range(a+1,N-1):
            for c in range(b+1,N):
                l=[L[a],L[b],L[c]]
                l.sort()
                print(l)
                if l[2] < l[0]+l[1]:
                    cnt+=1
                    triangle.append(l)
        print(triangle)
        ans=max(ans,cnt)

    print(ans)

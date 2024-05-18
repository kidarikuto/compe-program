# import my_func
import math 
import sys
import itertools
import bisect
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter

if __name__ == '__main__':
    S=input()
    T=input()
    T=T.lower()
    flag=0
    cnt=0
    search=T[cnt]
    for i in range(len(S)):
        if search==S[i]:
            cnt+=1
            if cnt==3:
                break
            search=T[cnt]
        
    if (cnt==2 and T[2]=="x") or cnt==3:
        print("Yes")
    else:
        print("No")
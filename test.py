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
    n=int(input())
    ans=0
    for i in range(1,n+1):
        if i%2==1:
            cnt=0
            for j in range(1,i+1):
                if i%j==0:
                    cnt+=1
            if cnt==8:
                ans+=1
    print(ans)
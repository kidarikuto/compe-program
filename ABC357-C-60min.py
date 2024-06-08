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
import numpy as np

def dfs_template(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # 訪問したノードの処理

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_template(graph, neighbor, visited)

##ABC342-C-TLE
if __name__ == '__main__':
    k=int(input())
    if k==0:
        print("#")
    elif k==1:
        print("###")
        print("#.#")
        print("###")
    else:
        ans=[["#" for i in range(3**k)] for j in range(3**k)]
        three=[3**i for i in range(k)]
        
        for i in range(3**k):
            for j in range(3**k):
                # if i%3**k>=3**(k-1) or j%3**k>=3**(k-1) or i%3**k<2*3**(k-1)-1 or j%3**k<2*3**(k-1)-1:
                #     ans[i][j]="."
                if i%3==1 and j%3==1:
                    ans[i][j]="."
                elif (i%3**2>=3**1 and i%3**2<2*(3**1)) and (j%3**2>=3**1 and j%3**2<2*(3**1)):
                    ans[i][j]="."
                elif (i%3**3>=3**2 and i%3**3<2*(3**2)) and (j%3**3>=3**2 and j%3**3<2*(3**2)):
                    ans[i][j]="."
                elif (i%3**4>=3**3 and i%3**4<2*(3**3)) and (j%3**4>=3**3 and j%3**4<2*(3**3)):
                    ans[i][j]="."
                elif (i%3**5>=3**4 and i%3**5<2*(3**4)) and (j%3**5>=3**4 and j%3**5<2*(3**4)):
                    ans[i][j]="."
                elif (i%3**6>=3**5 and i%3**6<2*(3**5)) and (j%3**6>=3**5 and j%3**6<2*(3**5)):
                    ans[i][j]="."

            print("".join(ans[i]))            



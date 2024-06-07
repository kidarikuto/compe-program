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
    line=input()
    line=list(line)
    num_type=set(line)
    cnt={i:0 for i in num_type}
    for i in line:
        cnt[i]+=1
    hahumann=[[] for i in range(10)]
    state=list(cnt.values())
    state.sort(reverse=True)
    print(line)
    print(state)
    print(cnt)
    print(hahumann)

    def find_key(cnt,value):
        for k,v in cnt.items():
            if v==value:
                return k
    if len(state)==1:
        hahumann[dic[state[0]]]=1
        for i in range(10):
            if hahumann[i]==[]:
                print(i," null")
            else:
                print(i,"",0)
    else:
        while len(state)>1:
            # print(state)
            a_num=state.pop()
            b_num=state.pop()
            c_num=a_num+b_num
            state.append(c_num)
            state.sort(reverse=True)
            a=find_key(cnt,a_num)
            del cnt[a]
            b=find_key(cnt,b_num)
            del cnt[b]
            c=a+b
            
            cnt[c]=c_num
            a_list=[int(char) for char in a]
            for i in a_list:
                hahumann[i].append(0)
            b_list=[int(char) for char in b]
            for i in b_list:
                hahumann[i].append(1)
            print(state)
            print(cnt)
            print(hahumann)
        for i in range(10):
            if hahumann[i]==[]:
                print(i," null")
            else:
                # print(hahumann[i])
                ans=hahumann[i][::-1]
                print(ans)
                ans=''.join(map(str,ans))
                print(i,"",ans)
                






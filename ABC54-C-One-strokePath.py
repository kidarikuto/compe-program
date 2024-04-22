# import my_func
import math 
import sys
from itertools import permutations
from itertools import combinations


# def sum_of_digits_19(num):
#     tmp = 0
#     for i in str(num):
#         if int(i) == 0:
#             return -1
#         else:
#             tmp += int(i)
#     return tmp
# def sum_of_digits(num):
#     return sum(int(i) for i in str(num))

if __name__ == '__main__':
    N,M = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(M)]
    # print(graph)
    my_list = [i for i in range(N)]
    perm = permutations(my_list)
    ans=0
    for p in perm:
        if p[0] == 0:
            # print(p)
            flag = 1
            # print("p=",p)
            #全てのノードを1回ずつ通るパスの順列
            for i in range(N-1):
                edge_flag=0
                for j in range(M):
                    if (p[i]==graph[j][0]-1 and p[i+1]==graph[j][1]-1) or (p[i+1]==graph[j][0]-1 and p[i]==graph[j][1]-1):
                        # print(p[i],graph[j][0]-1,p[i+1],graph[j][1]-1)
                        edge_flag=1
                        break
                    else:
                        pass
                if edge_flag==0:
                    flag=0
                
            if flag == 1:
                ans += 1
            # print(ans)
    print(ans)
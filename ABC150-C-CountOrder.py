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
    N = int(input())

    p =input().split()
    q =input().split() 

    P = list(map(int,p))
    Q = list(map(int,q))
    

    my_list = [i for i in range(N)]
    perm = permutations(my_list)
    a=0 
    b=0
    cnt=0
    for p in perm:
        # print(p)
        cnt += 1
        for i in range(N):
            # print(p[i]+1,P[i])
            if i == N-1:
                a = cnt
            if p[i]+1 == P[i]:
                continue
            else:
                break
 

    cnt=0
    qerm = permutations(my_list)
    for q in qerm:
        # print(q)
        cnt += 1
        for i in range(N):
            # print(q[i]+1,Q[i])
            if i == N-1:
                b = cnt
            if q[i]+1 == Q[i]:
                continue
            else:
                break
            
    print(abs(a-b))
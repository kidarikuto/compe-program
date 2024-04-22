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
    location = [list(map(int,input().split())) for _ in range(N)]
    # print(location)
    my_list = [int(i) for i in range(N)]
    perm = permutations(my_list)
    ans = 0
    for p in perm:
        for i in range(N-1):
            x = (location[p[i]][0]-location[p[i+1]][0])**2
            y = (location[p[i]][1]-location[p[i+1]][1])**2
            dis = math.sqrt(x+y)
            # print(dis)
            ans += dis
    # print(math.factorial(N))
    print(ans/math.factorial(N))
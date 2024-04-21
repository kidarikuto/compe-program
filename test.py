# import my_func
import math 
import sys
from itertools import permutations
from itertools import combinations

# coding test

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
    data = [[[],[]] for _ in range(N)]
    for i in range(N):
        a = int(input())
        for _ in range(a):
            x,y = map(int,input().split())
            if y == 0:
                data[i][0].append(x-1)
            else:
                data[i][1].append(x-1)
    print(data)

    ans = 0
    for i in range(2**N):
        flag = 1
        cnt = 0
        for j in range(N):
            if i & (1 << j):
                for k in data[j][1]:
                    if i & (1 << k):
                        cnt += 1
                        continue
                    else:
                        flag = 0
                        break
        if flag:
            ans = max(ans,cnt)
    print(ans)
    #以下に追加したコードを書いていく
    print("add file")
    print("add file")
    print("add file")
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
    data = [[[],[]] for _ in range(N)]
    for i in range(N):
        a = int(input())
        for _ in range(a):
            x,y = map(int,input().split())
            if y == 0:
                data[i][0].append(x-1)
            else:
                data[i][1].append(x-1)
    # print(data)

    ans = 0
    for i in range(2**N):
        cnt = 0
        flag = 1
        # print("i=",i)
        #N人の証言者調査、正直者ならcnt+=1
        for j in range(N):
            # print(" j=",j)
            honest = 1
            if i & (1 << j):
                #証言者の正直者の判定
                for k in data[j][1]:
                    t = i & (1<<k)
                    # print("     k=",k,"i&(1<<k)",i & (1 << k))       
                    if (t>0) and honest:
                        continue
                    else:
                        flag = 0
                        honest = 0
                        cnt = 0
                        break
                #証言者の嘘つきの判定
                for k in data[j][0]:
                    t = i & (1<<k)
                    # print("     k=",k,"j=",j,"t",t)       
                    if (t==0) and honest:
                        continue
                    else:
                        flag = 0
                        honest = 0
                        cnt = 0
                        break
                if honest == 1:
                    cnt += 1 
            # print(" cnt=",cnt)
        if flag == 1:
            ans = max(ans,cnt)
    print(ans)
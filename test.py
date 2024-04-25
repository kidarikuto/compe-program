# import my_func
import math 
import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def sum_of_digits_19(num):
    tmp = 0
    for i in str(num):
        if int(i) == 0:
            return -1
        else:
            tmp += int(i)
    return tmp
def sum_of_digits(num):
    return sum(int(i) for i in str(num))

if __name__ == '__main__':
    L,R=map(int,input().split())
    ans = 10**9
    l = L%2019
    k = L//2019 + 1
    if 2019*k <= R:
        print(0)
    else:
        t = L%2019
        print((L*(L+1))%2019)
    # for l in range(L,R):
    #     for r in range(l+1,R+1):
    #         ans = min(ans,(l*r)%2019)
    # print(ans)

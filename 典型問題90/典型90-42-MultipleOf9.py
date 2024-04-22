#import my_func
import math
from itertools import permutations

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

# point
# 桁和or桁数のどちらを動的にするか⇒桁和を動かす、桁数は無視
if __name__ == '__main__':
    K = int(input())
    cnt = 0
    # print(sum_of_digits(K))
    if sum_of_digits(K)%9 != 0:
        print(0)
    else:#Kが9の倍数<=>Xの各桁の総和も9の倍数
        dp = [0 for i in range(K+1)]
        dp[0] = 1
        # dp[K//9]=1
        # for i in range(K//9+1,K+1):
        #     dp[i] = dp[i-1] + (9**(i-1) - dp[i-1])
        # print(dp[1],dp[2],dp[3])
        # print(sum(dp)%(10**9+7))

        for i in range(1,K+1):
            if i <= 9:
                dp[i] = sum(dp)
            else:
                dp[i]=sum(dp[i-9:i])
        print(dp[K]%(10**9+7))
        # print(dp)
        
        

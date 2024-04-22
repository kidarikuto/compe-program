#自作関数のインポート
#import my_func
import math


#整数で処理すれば誤差をなくすことができる
if __name__ == '__main__':
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    cost = 0
    for i in range(N):
        cost += abs(A[i]-B[i])
    if ((K-cost) >= 0) and ((K-cost)%2==0):
        print("Yes")
    else:
        print("No")

    
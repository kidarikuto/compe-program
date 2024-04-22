#自作関数のインポート
#import my_func
import math


#整数で処理すれば誤差をなくすことができる
if __name__ == '__main__':
    N = int(input())
    user = {}
    for i in range(N):
        s = str(input())
        if s in user:
            pass
        else:
            user.setdefault(s,1)
            print(i+1)
    
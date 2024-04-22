#自作関数のインポート
#import my_func
import math


#整数で処理すれば誤差をなくすことができる
if __name__ == '__main__':
    a,b,c = map(int,input().split())
    if a < c**b:
        print("Yes")
    else:
        print("No")
    
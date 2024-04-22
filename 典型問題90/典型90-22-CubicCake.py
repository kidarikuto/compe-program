#自作関数のインポート
#import my_func
import math


#整数で処理すれば誤差をなくすことができる
if __name__ == '__main__':
    a,b,c = map(int,input().split())
    gcd_ab = math.gcd(a,b)
    gcd_abc = math.gcd(gcd_ab,c)
    if gcd_abc == 1:
        print(a+b+c-3)
    else:
        ans = int(a/gcd_abc + b/gcd_abc + c/gcd_abc -3)
        print(ans)
    
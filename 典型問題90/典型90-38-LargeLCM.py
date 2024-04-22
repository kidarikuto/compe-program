#自作関数のインポート
#import my_func
import math
from itertools import permutations


# point
if __name__ == '__main__':
    A,B = map(int,input().split())
    ceil = 10**18
    ans = A*B//math.gcd(A,B)
    
    if ans > ceil:
        print("Large")
    else:
        print(ans)
    
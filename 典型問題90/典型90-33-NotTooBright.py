#自作関数のインポート
#import my_func
import math
from itertools import permutations


# point
# コーナーケースに気を付ける
# 今回の場合1列の場合は縦横2*2の領域がないから全灯させても問題ない
if __name__ == '__main__':
    H,W = map(int,input().split())
    if H==1 or W==1:
        ans = H*W
    else:
        ans = math.ceil(H/2) * math.ceil(W/2)
    print(ans)
    
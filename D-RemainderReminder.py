input_data = input()
N, K = map(int, input_data.split())

count = 0
if K == 0:
    count = N*N
    print(count)
elif K > 0:
    for b in  range(K+1,N+1):
        d = 0
        n = int((N+1)/b)
        d += n*(b-K)

        s = K + n*b
        l = N
        if s <= l:
            d += l - s +1
        count += d
    print(count)

"""
余りがK以上ないといけないのでbの探索範囲はK+1 ~ Nまで
aについて
b以下で条件に合うものはK ~ b-1なのでdに追加
このK ~ b-1に+bしても余りは変わらないので
aの探索範囲は
K ~ b-1
K+b ~ 2*b-1
・
・
・
K+(n-1) ~ n*b-1
であるがnb-1がNを超える場合があるので最後の条件分岐は
その場合を考慮している
"""
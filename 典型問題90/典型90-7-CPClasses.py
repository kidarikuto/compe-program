from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()

if len(A) != N:
    print("eroor")
else:
    Q = int(input())
    B = []
    for j in range(Q):
        b = int(input())
        j = bisect_left(A,b)

        res = 2**60
        if j < N:
            res = min(res,abs(b-A[j]))
        if j > 0:
            res = min(res, abs(b-A[j-1]))
        print(res)
        # 0 1 2    N-2 N-1
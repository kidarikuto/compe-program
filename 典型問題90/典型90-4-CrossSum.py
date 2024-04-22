H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

B = []
for i in range(H):
    tmp = []
    for j in range(W):
        col = sum(list(zip(*A))[j])
        row = sum(A[i])
        tmp.append(row+col-A[i][j])
    print(" ".join(map(str,tmp)))

# for row in B:
    # print(" ".join(map(str, row)))

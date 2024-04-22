from itertools import product

def func(x):
    cnt = 0
    for i in range(len(x)):
        if x[i] == "(":
            cnt += 1
        elif x[i] == ")":
            cnt -= 1
        if cnt < 0:
            return 0
    if cnt == 0:
        return 1
    else:
        return 0

N = int(input())
result = [''.join(map(str, item)) for item in product(['(',')'], repeat=N)]

for i in range(len(result)):
    if func(result[i]) == 1:
        print(result[i])
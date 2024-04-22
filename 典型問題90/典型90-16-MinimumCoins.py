#自作関数のインポート
#import my_func

if __name__ == '__main__':
    N = int(input())
    A,B,C = map(int,input().split())
    max_ans = 9999
    ans = max_ans
    for i in range(max_ans):
        for j in range(max_ans):
            tmp = N - A*i - B*j
            if (tmp < 0) or (tmp % C != 0):
                continue
            k = tmp//C
            if ans > i + j + k:
                ans = i + j + k
    print(ans)
    
    

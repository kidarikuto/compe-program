#自作関数のインポート
#import my_func

if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    diff = [abs(a - b) for a, b in zip(A, B)]
    total_sum = sum(diff)
    print(total_sum)



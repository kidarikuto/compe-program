#自作関数のインポート
#import my_func

if __name__ == '__main__':
    N = int(input())
    score = [[0,0]]
    for i in range(1,N+1):
        c,p = map(int,input().split())
        if c == 1:
            score.append([score[i-1][0]+p, score[i-1][1]])
        elif c == 2:
            score.append([score[i-1][0], score[i-1][1]+p])
        
    q = int(input())
    for i in range(q):
        l,r = map(int,input().split()) 
        print(score[r][0]-score[l-1][0], score[r][1]-score[l-1][1])
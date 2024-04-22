#自作関数のインポート
#import my_func
import math

if __name__ == '__main__':
    T = int(input())
    L,X,Y = map(int,input().split())
    Q = int(input())
    for _ in range(Q):
        e = int(input())
        theata = 360*e/T
        rad = 2*math.pi*theata/360
        #print(theata)
        y = (-math.sin(rad))*L/2
        z = (1 - math.cos(rad))*L/2
        #print(y,z)
        result = math.atan(z/math.sqrt(X**2 + (Y-y)**2))
        print(result*180/math.pi)
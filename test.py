# import my_func
import math 
import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def val_cal(num):
    c=str(num)
    digit=len(c)
    return A*num+B*digit
if __name__ == '__main__':
    A,B,X=map(int,input().split())
    ans=10**9
    num_digit=1
    # val_cal=A*ans+B+10
    if val_cal(ans)<=X:
        print(ans)
    elif A+B>X:
        print(0)
    else:
        next=int(ans/2)
        while(1):
            if val_cal(next)>X:
                ans=next
                next=int(next/2)
                # print("next=",next)
            elif val_cal(next)<=X:
                next=int((next+ans)/2)
                # print("next=",next)
                # print("ans=",ans)
                if ans-next==1 and val_cal(next)<=X:
                    print(next)
                    break
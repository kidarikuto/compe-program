import sys

input_data = input()
n, m = map(int, input_data.split())
cnt =0
if n==1 and m==1:
    cnt = 1
elif n==1 and m>=2:
    cnt = m-2
elif m==1 and n>=2:
    cnt = n-2
else:
    cnt = n*m - (2*(n+m)-4)
print(cnt)



"""
    m列  
    0  j  m-1
n行 ーーーー
0   ー〇〇ー
i   ー〇〇ー
n-1 ーーーー    

[i-1,j-1] [i-1,j] [i-1,j+1]
[  i,j-1] [  i,j] [  i,j+1]
[i+1,j-1] [i+1,j] [i+1,j+1]

ーーーーーーーーー
ー〇〇〇〇〇〇〇ー
ーーーーーーーーー

elif n==1 and m>=2:
            if j==0 or j==m-1:
                grid[i][j] =1
            else:
                grid[i][j] =-1
                cnt+=1
        elif m==1 and n>=2:
            if i==0 or i==n-1:
                grid[i][j] =1
            else:
                grid[i][j] =-1
                cnt+=1

"""



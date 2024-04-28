import sys

"""
# 引数の数を表示
print("Number of arguments:", len(sys.argv) - 1)
# 引数を表示
for i in range(1, len(sys.argv)):
    #print(f"Argument {i}: {sys.argv[i]}")
    pass
a = int(sys.argv[1])
b = int(sys.argv[2])
"""

input_data = input()
a, b = map(int, input_data.split())
#print("A:",a)
#print("B:",b)
cnt = 0
A = str(a)
B = str(b)
for i in range(a,b+1):
    I = str(i)
    half_len = int(len(I)/2)
    #print(i)
    flag = True
    for j in range(0,half_len):
        if I[j] != I[len(I)-1-j]:
            flag = False
            break
    if flag == True:
        cnt += 1
print(cnt)

"""
 0  1  2  3  4
-5 -4 -3 -2 -1 
"""




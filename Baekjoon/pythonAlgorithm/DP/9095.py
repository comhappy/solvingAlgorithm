# 1,2,3 더하기

import sys
input = sys.stdin.readline

def DP(n):
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        num = [0 for _ in range(n + 1)]

        num[1] = 1  # 1
        num[2] = 2  # 1+1, 2
        num[3] = 4  # 1+1+1, 1+2, 2+1, 3

        for i in range(4, n + 1):
            num[i] = num[i - 1] + num[i - 2] + num[i - 3]

        print(num[n])


t = int(input())

for _ in range(t):
    n = int(input())

    DP(n)
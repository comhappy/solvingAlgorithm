# 파도반 수열

import sys
input = sys.stdin.readline

def DP(n):
    num = [0, 1, 1, 1, 2, 2]

    if n < 6:
        print(num[n])
    else:
        for i in range(6, n + 1):
            num.append(num[i - 1] + num[i - 5])

        print(num[n])


t = int(input())

for _ in range(t):
    n = int(input())

    DP(n)
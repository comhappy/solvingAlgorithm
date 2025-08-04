# 2xn 타일링 2

import sys
input = sys.stdin.readline

def DP(n):
    answer = [0 for _ in range(n + 1)]

    answer[1] = 1
    answer[2] = 3

    for i in range(3, n + 1):
        answer[i] = (answer[i - 1] + answer[i - 2] * 2) % 10007

    print(answer[n])


n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    DP(n)
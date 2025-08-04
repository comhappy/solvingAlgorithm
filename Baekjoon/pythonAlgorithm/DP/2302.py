# 극장 좌석

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [1 for _ in range(n + 1)]  # dp[i]는 vip자리가 없을 때, i번째 자리까지 앉을 수 있는 경우의 수

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]   # i번째 자리를 고정하는 경우 + i번째 자리를 고정하지 않는 경우

answer = 1
s = 1

for _ in range(m):
    e = int(input())
    answer *= dp[e - s]
    s = e + 1

answer *= dp[n + 1 - s]

print(answer)
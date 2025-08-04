# 1, 2, 3 더하기 4

import sys
input = sys.stdin.readline

t = int(input())
n = list()

for _ in range(t):
    n.append(int(input()))

dp = [1 for _ in range(max(n) + 1)] # 1로만 이루어진 경우, dp[i]는 i를 만드는 경우의 수


for i in range(2, max(n) + 1):  # 2를 추가하는 경우
    dp[i] += dp[i - 2]

for i in range(3, max(n) + 1):  # 3를 추가하는 경우
    dp[i] += dp[i - 3]


print(dp)

for i in n:
    print(dp[i])
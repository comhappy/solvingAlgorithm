# 줄세우기

import sys
input = sys.stdin.readline

n = int(input())
line = list()

for _ in range(n):
    line.append(int(input()))

dp = [1 for _ in range(n)]  # LIS를 나타내는 DP 배열

for i in range(1, n):
    for j in range(i):
        if line[i] > line[j]:
            dp[i] = max(dp[i], dp[j] + 1)   # 최대 LIS 저장

print(n - max(dp))
# 퇴사2

import sys
input = sys.stdin.readline

def DP():
    dp = [0 for _ in range(n + 1)]  # i일차에 얻을 수 있는 최대 이익

    for i in range(1, n + 1):
        if time[i - 1]:
            for j in time[i - 1]:
                t, p = j

                dp[i] = max(dp[i], dp[i - t] + p, dp[i - 1])    # 원래값, 상담을 선택했을때, 상담을 선택 안했을때
        else:
            dp[i] = max(dp[i], dp[i - 1])

    print(dp[n])


n = int(input())

time = [[] for _ in range(n)]   # i일차에 얻을 수 있는 이익

for i in range(n):
    t, p = map(int, input().split())

    if i + t - 1 < n:
        time[i + t - 1].append([t, p])

DP()
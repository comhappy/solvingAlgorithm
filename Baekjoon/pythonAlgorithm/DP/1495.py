# 기타리스트

import sys
input = sys.stdin.readline

def DP():
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    dp[0][s] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            if 0 <= j - v[i] <= m:
                if dp[i - 1][j - v[i]] == 1:
                    dp[i][j] = 1

            if 0 <= j + v[i] <= m:
                if dp[i - 1][j + v[i]] == 1:
                    dp[i][j] = 1

        if sum(dp[i]) == 0: # 가능한 경우가 없는 경우
            print(-1)

            return

    # 정답 볼륨을 출력
    for i in range(m, -1, -1):
        if dp[n][i] == 1:
            print(i)
            return
        

n, s, m = map(int, input().split())
v = [0] + list(map(int, input().split()))

DP()
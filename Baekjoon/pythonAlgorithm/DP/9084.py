# 동전

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  # i원을 만드는 개수를 저장하는 dp 배열

    # 기저상태 저장
    for i in range(1, n + 1):
        if coin[i - 1] <= m:
            dp[i][coin[i - 1]] = 1
            dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j > coin[i - 1]:    # 동전이 더 작은 경우, 나머지 값으로 만들 수 있음
                dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i - 1]]    # 해당 동전을 사용하는 경우 + 사용하지 않는 경우
            else:   # 동전이 더 큰 경우
                dp[i][j] += dp[i - 1][j]

    print(dp[n][m])
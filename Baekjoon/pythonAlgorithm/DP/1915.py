# 가장 큰 정사각형

n, m = map(int, input().split())
A = list(list(map(int, list(input()))) for _ in range(n))

# DP적인 생각
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
answer = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        if answer < dp[i][j]:
            answer = dp[i][j]

print(answer ** 2)
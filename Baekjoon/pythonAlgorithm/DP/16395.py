n, k = map(int, input().split())

dp = [[0 for _ in range(n)] for _ in range(k)]

# 기저상태 저장
for i in range(k):
    dp[i][i] = 1

for i in range(n):
    dp[0][i] = 1

# 나머지 dp 테이블 채우기
for i in range(1, k):
    for j in range(i + 1, n):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

print(dp[k - 1][n - 1])
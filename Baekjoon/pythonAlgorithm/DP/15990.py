# 1, 2, 3 더하기 5

dp = [[0 for _ in range(4)] for _ in range(100001)] # dp[i][j] : 합을 i로 만들 때, j로 끝나는 수

dp[1][1] = 1    # 1
dp[1][2] = 0
dp[1][3] = 0

dp[2][1] = 0
dp[2][2] = 1    # 2
dp[2][3] = 0

dp[3][1] = 1    # 2 + 1
dp[3][2] = 1    # 1 + 2
dp[3][3] = 1    # 3

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % 1000000009
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % 1000000009
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % 1000000009


t = int(input())

for _ in range(t):
    n = int(input())

    print(sum(dp[n]) % 1000000009)
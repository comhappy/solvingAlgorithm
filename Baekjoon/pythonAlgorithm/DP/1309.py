# 동물원

n = int(input())

dp = [[1 for _ in range(n + 1)] for _ in range(3)]  # 세로 index = (왼쪽에 놓기, 오른쪽에 놓기, 안놓기)

for i in range(2, n + 1):
    dp[0][i] = (dp[1][i -1] + dp[2][i - 1]) % 9901   # 왼쪽에 놓기
    dp[1][i] = (dp[0][i -1] + dp[2][i - 1]) % 9901   # 오른쪽에 놓기
    dp[2][i] = (dp[0][i - 1]+ dp[1][i -1] + dp[2][i - 1]) % 9901   # 안놓기

answer = (dp[0][n] + dp[1][n] + dp[2][n]) % 9901
print(answer)
# 점프점프

n = int(input())
A = list(map(int, input().split()))

dp = [-1 for _ in range(n)]
dp[0] = 0

for i in range(n):
    if dp[i] != -1: # 방문할 수 있는 경우
        for j in range(1, A[i] + 1):
            if i + j < n:
                if dp[i + j] == -1:
                    dp[i + j] = dp[i] + 1
                else:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[n - 1])
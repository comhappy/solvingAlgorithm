# 오르막 수

def DP():
    dp = [1 for _ in range(10)]

    for _ in range(n - 1):
        for i in range(1, 10):
            dp[i] = (dp[i - 1] + dp[i])

    print(sum(dp) % 10007)
        

n = int(input())
DP()
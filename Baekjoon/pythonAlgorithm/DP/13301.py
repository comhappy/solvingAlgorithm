# 타일 장식물

n = int(input())

if n == 1:
    print(4)
else:
    dp = [0 for _ in range(n + 1)]
    
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(4 * dp[n] + 2 * dp[n - 1])
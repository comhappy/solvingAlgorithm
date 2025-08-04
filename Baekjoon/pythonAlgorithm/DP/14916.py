# 거스름돈

n = int(input())

dp = [0, -1, 1, -1, 2, 1, 3, 2, 4]

for i in range(9, n + 1):
    count = min(dp[i - 2], dp[i - 5])
    dp.append(count + 1)

print(dp[n])
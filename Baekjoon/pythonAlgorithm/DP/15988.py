# 1,2,3 더하기 3

answer = list()

t = int(input())

for _ in range(t):
    answer.append(int(input()))

dp = [1, 1, 2]

for i in range(3, max(answer) + 1):
    dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009)

for i in answer:
    print(dp[i])
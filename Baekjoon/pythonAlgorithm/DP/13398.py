# 연속합 2

n = int(input())
num = [0] + list(map(int, input().split()))

# dp[0][i]는 1 ~ i까지 합(숫자를 빼지 않은 경우), dp[1][i]는 1 ~ i까지 합(숫자를 하나 뺀 경우)
dp = [[0 for _ in range(n + 1)] for _ in range(2)]

result = num[1]
dp[0][1] = num[1]
dp[1][1] = num[1]

for i in range(2, n + 1):
    dp[0][i] = max(dp[0][i - 1] + num[i], num[i])   # 앞서나온 연속합 vs i번째 숫자
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + num[i]) # i번째 숫자를 뺀 경우 vs i번째 숫자를 넣은 경우

    result = max(result, dp[0][i], dp[1][i])

print(result)
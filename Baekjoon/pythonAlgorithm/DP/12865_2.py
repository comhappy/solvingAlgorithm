# 평범한 배낭

n, k = map(int, input().split())
weigh, value = list(), list()

for _ in range(n):
    w, v = map(int, input().split())

    weigh.append(w)
    value.append(v)

# DP를 이용한 배낭문제 해결

dp = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(k + 1):
    if i >= weigh[0]:
        dp[0][i] = value[0]

for i in range(1, n):
    for j in range(k + 1):
        if j >= weigh[i]:   # 가방에 넣을 수 있는 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weigh[i]] + value[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n - 1][k])
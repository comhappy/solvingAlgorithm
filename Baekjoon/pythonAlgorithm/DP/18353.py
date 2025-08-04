# 병사 배치하기

n = int(input())
force = list(map(int, input().split()))

dp = [1 for _ in range(n)]  # dp[i] : i번째 병사를 사용할 때, 최대 병사 수

for i in range(1, n):
    for j in range(i):
        if force[i] < force[j]: # i번째 병사를 사용하는 경우
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) 
# 카드 구매하기 2

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # 가로줄은 카드 장수를 뜻함, 세로줄은 사용할 수 있는 카드팩을 뜻함

# 기저상태 저장
for i in range(1, n + 1):
    dp[1][i] = p[1] * i

for i in range(2, n + 1):
    for j in range(1, n + 1):
        # dp[i][j]는 i까지 카드팩을 사용했을때 j장의 카드를 만드는 최소 비용을 뜻함
        if j - i >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - i] + p[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][n])

#====================================================================================

# 카드 구매하기 2

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [i for i in p]

for i in range(1, n + 1):
    for j in range(i):
        dp[i] = min(dp[i], dp[i - j] + p[j])

print(dp[n])
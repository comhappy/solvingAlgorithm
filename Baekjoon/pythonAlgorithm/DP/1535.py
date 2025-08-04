# 안녕

n = int(input())
life = list(map(int, input().split()))
point = list(map(int, input().split()))

# 최대 기쁨을 의미, dp[i][j] 의미 : i번째 사람까지 인사하고 잃은 체력이 j일때, 얻을 수 있는 최대 기쁨
dp = [[0 for _ in range(101)] for _ in range(n + 1)]  

for i in range(n):
    dp[i + 1][life[i]] = point[i]

for i in range(1, n + 1):
    for j in range(101):
        if 0 <= j - life[i - 1] < 101:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - life[i - 1]] + point[i - 1])
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[n][:100]))
# 로봇 조종하기

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

dp = [0 for _ in range(m)]  # 최종으로 가질 수 있는 최대 값
dp_right = [0 for _ in range(m)]  # 오른쪽으로 이동시 가질 수 있는 최대 값
dp_left = [0 for _ in range(m)]  # 왼쪽으로 이동시 가질 수 있는 최대 값

# 기저상태 저장
dp[0] = graph[0][0]

for i in range(1, m):
    dp[i] = dp[i - 1] + graph[0][i]

for i in range(1, n):
    for j in range(m):  # 오른쪽으로 이동시 dp 테이블 결정
        if j == 0:
            dp_right[j] = dp[j] + graph[i][j]
        else:
            dp_right[j] = max(dp[j], dp_right[j - 1]) + graph[i][j]

    for j in range(m - 1, -1, -1):  # 왼쪽으로 이동시 dp 테이블 결정
        if j == m - 1:
            dp_left[j] = dp[j] + graph[i][j]
        else:
            dp_left[j] = max(dp[j], dp_left[j + 1]) + graph[i][j]

    for j in range(m):  # 최종 dp 테이블 결정
        dp[j] = max(dp_right[j], dp_left[j])

print(dp[m - 1])
# 호텔

c, n = map(int, input().split())
info = [[0, 0]]

# info[x][0] : 비용, info[x][1] : 고객 수
for _ in range(n):
    info.append(list(map(int, input().split())))

# dp[i][j] : i번째 도시정보를 사용해서 j명의 인원을 만들 때, 구할 수 있는 최소비용
dp = [[1000 * 100 for _ in range(1101)] for _ in range(n + 1)]

# 초기값 설정
for i in range(1, n + 1):
    x = info[i][1]
    y = info[i][0]
    j = 1

    while(x * j <= 1100):
        dp[i][x * j] = y * j
        j += 1

# 나머지 dp 배열 채우기
for i in range(1, n + 1):
    for j in range(1, 1101):
        # dp[i - 1][j]    # 사용하지 않을 때
        # dp[i][j - info[i][1]] + info[i][0]         # 사용할 때

        if j - info[i][1] >= 0:  # item을 사용할 수 있는 경우
            dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i][j - info[i][1]] + info[i][0])
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
                
answer = 1000 * 100

# 정답 구하기
for i in range(c, 1101):
    for j in range(n + 1):
        answer = min(answer, dp[j][i])

print(answer)
# 자두나무

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
point = [0]

for _ in range(t):
    point.append(int(input()))
    
# dp[t][1][w]는 t초 후 w번 움직였을때, 1번나무에 있는 경우 자두의 개수
# dp[t][2][w]는 t초 후 w번 움직였을때, 2번나무에 있는 경우 자두의 개수
dp = [[[-1 for _ in range(w + 1)] for _ in range(3)] for _ in range(t + 1)] # -1은 이동할 수 없음

dp[0][1][0] = 0 # 기저상태

for i in range(1, t + 1):
    # j == 0인 경우, 0번 이동하는 경우
    dp[i][1][0] = dp[i - 1][1][0]

    if point[i] == 1:
        dp[i][1][0] += 1

    for j in range(1, w + 1):
        if j > i:
            break

        dp[i][1][j] = max(dp[i - 1][2][j - 1], dp[i - 1][1][j]) # 이동하는 경우 vs 이동하지 않는 경우
        dp[i][2][j] = max(dp[i - 1][1][j - 1], dp[i - 1][2][j])

        if dp[i][point[i]][j] != -1:
            dp[i][point[i]][j] += 1 # 떨어지는 자두 먹기
        
answer = max(max(dp[t][1]), max(dp[t][2]))
print(answer)
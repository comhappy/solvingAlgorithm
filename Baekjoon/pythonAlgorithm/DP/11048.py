# 이동하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(x, y):
    if x == n - 1 and y == m - 1:   # 종료조건
        return miro[x][y]
    
    if visited[x][y] == -1:  # 방문하지 않은 경우
        visited[x][y] = 0

        candy = 0

        for dx, dy in [[0, 1], [1, 0]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m: # 좌표를 만족하는 경우
                candy = DFS(nx, ny) + miro[x][y]

            visited[x][y] = max(visited[x][y], candy)
    
    return visited[x][y]


def DP():
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):	# DP 테이블에 사탕 개수 복사
        for j in range(1, m + 1):
            dp[i][j] = miro[i - 1][j - 1]

    for i in range(1, n + 1):	# DP 테이블 채우기
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + dp[i][j]

    print(dp[n][m])

n, m = map(int, input().split())
miro = list(list(map(int, input().split())) for _ in range(n))
visited = [[-1 for _ in range(m)] for _ in range(n)]

DFS(0, 0)
print(visited[0][0])

DP()
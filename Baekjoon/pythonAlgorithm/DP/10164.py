# 격자상의 경로

def DFS(x, y):
    if visited[x][y] == 1:  # 방문한 경우
        return dp[x][y]
    else:
        visited[x][y] = 1

        for dx, dy in [[1, 0], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < kn and 0 <= ny < km:
                dp[x][y] += DFS(nx, ny)

        return dp[x][y]
    

n, m, k = map(int, input().split())

if k == 0:  # O표시 칸이 없는 경우
    kn, km = n, m
    dp = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dp[n - 1][m - 1] = 1

    answer = DFS(0, 0)

    print(answer)
else:
    if k % m == 0:
        kn = k // m
        km = m
    else:
        kn = k // m + 1
        km = k % m

    dp = [[0 for _ in range(km)] for _ in range(kn)]
    visited = [[0 for _ in range(km)] for _ in range(kn)]
    dp[kn - 1][km - 1] = 1

    answer = DFS(0, 0)

    kn, km = n - kn + 1, m - km + 1
    dp = [[0 for _ in range(km)] for _ in range(kn)]
    visited = [[0 for _ in range(km)] for _ in range(kn)]
    dp[kn - 1][km - 1] = 1

    answer *= DFS(0, 0)

    print(answer)
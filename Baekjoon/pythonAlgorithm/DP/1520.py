# 내리막 길
import sys
sys.setrecursionlimit(10 ** 6)

def DFS(x, y):
    if x == m - 1 and y == n - 1:   # 도착지에 도착
        return 1
    if visited[x][y] == -1: # 방문하지 않은 경우
        visited[x][y] = 0

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n: # 좌표를 만족하는 경우
                if graph[x][y] > graph[nx][ny]:    # 내리막인 경우
                    visited[x][y] += DFS(nx, ny)

    return visited[x][y]
                    

m, n = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(m))
visited = [[-1 for _ in range(n)] for _ in range(m)]

DFS(0, 0)

print(visited[0][0])
# 쉬운 최단거리

from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    answer = [[-1 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                answer[i][j] = 0

    visited = [[0 for _ in range(m)] for _ in range(n)]

    que = deque()

    que.append([x, y])
    visited[x][y] = 1
    answer[x][y] = 0

    while(que):
        x, y = que.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    que.append([nx, ny])
                    visited[nx][ny] = 1
                    answer[nx][ny] = answer[x][y] + 1

    return answer

n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            result = BFS(i, j)
            break

for i in result:
    print(*i)
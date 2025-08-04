# 보물섬

from collections import deque
import sys
input = sys.stdin.readline


def BFS(x, y):
    que = deque()
    visited_BFS = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0

    que.append([x, y, 0])
    visited_BFS[x][y] = 1

    while(que):
        x, y, depth = que.popleft()

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == "L" and visited_BFS[nx][ny] == 0:
                    answer = depth + 1
                    que.append([nx, ny, depth + 1])
                    visited_BFS[nx][ny] = 1

    return answer


n, m = map(int, input().split())
graph = list(list(input().strip()) for _ in range(n))
result = 0

for i in range(n):
    for j in range(m):
        # BFS를 이용해서 최대거리 찾기
        if graph[i][j] == "L":
            result = max(result, BFS(i, j))

print(result)
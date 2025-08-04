# 빙산

from collections import deque
import sys
input = sys.stdin.readline

def melting(graph): # 빙하 녹이기
    new_graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:    # 빙산인 경우
                new_ice = graph[i][j]

                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:   # 4방향 탐색
                    nx, ny = i + dx, j + dy

                    if graph[nx][ny] == 0:  # 바다인 경우
                        new_ice -= 1

                        if new_ice == 0:
                            break

                new_graph[i][j] = new_ice

    return new_graph

def BFS(i, j):  # BFS를 활용한 빙산 탐색
    que = deque()
    que.append([i, j])
    visited[i][j] = 1

    while(que):
        x, y = que.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:   # 4방향 탐색
            nx, ny = x + dx, y + dy

            if graph[nx][ny] != 0 and visited[nx][ny] == 0:  # 빙산인 경우
                que.append([nx, ny])
                visited[nx][ny] = 1


n, m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
visited = [[0 for _ in range(m)] for _ in range(n)]

count = 0   # 빙산의 개수
years = 0   # 소요되는 년

while(1):
    graph = melting(graph)
    years += 1
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                BFS(i, j)
                count += 1

    if count == 0 or count >= 2:    # 종료 조건
        break
    
    visited = [[0 for _ in range(m)] for _ in range(n)]

if count >= 2:
    print(years)
else:
    print(0)
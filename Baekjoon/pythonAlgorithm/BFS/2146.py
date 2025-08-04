# 다리 만들기

from collections import deque
import sys, copy
input = sys.stdin.readline

def BFS_side(x, y):
    # 테두리 검출
    visited_land = [[0 for _ in range(n)] for _ in range(n)]

    que_side = deque()  # 테두리 좌표를 저장하는 큐
    que = deque()   # 테두리 검사를 위한 큐
    que.append([x, y])
    visited_land[x][y] = 1
    visited[x][y] = 1

    # 테두리 찾기
    while(que):
        x, y = que.popleft()

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited_land[nx][ny] == 0:
                    if graph[nx][ny] == 1:  # 주변이 섬인 경우 = 다음에 탐색하는 섬
                        que.append([nx, ny])
                        visited_land[nx][ny] = 1
                        visited[nx][ny] = 1
                    else:   # 주변이 바다인 경우 = 테두리
                        if [x, y, 0] not in que_side:
                            que_side.append([x, y, 0])

    return que_side, visited_land

def BFS(que_side, visited_land):
    # 최단거리 다리 찾기
    global answer

    while(que_side):
        x, y, length = que_side.popleft()

        if length > answer: # 다리 길이가 최소 다리길이보다 큰 경우
            return

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited_land[nx][ny] == 0:
                    if graph[nx][ny] == 0:  # 바다인 경우
                        que_side.append([nx, ny, length + 1])
                        visited_land[nx][ny] = 1
                    elif graph[nx][ny] == 1:    # 다른 섬인 경우
                        answer = length

                        return


n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

visited = [[0 for _ in range(n)] for _ in range(n)]
answer = n * n

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:    # 섬인 경우
            que_side, visited_land = BFS_side(i, j)
            BFS(que_side, visited_land)

print(answer)
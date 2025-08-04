# 미세먼지 안녕!

import sys, copy
input = sys.stdin.readline

def spread(graph):   # 미세먼지 확산
    copy_graph = copy.deepcopy(graph)

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if graph[i][j] != -1 and graph[i][j] != 0:  # 빈칸, 공기청정기가 아닌 경우
                count = 0   # 확산되는 칸의 개수
                dust = int(graph[i][j] // 5)    # 확산되는 미세먼지 양

                for dx, dy in [[0, 1], [0, - 1], [1, 0], [-1, 0]]:
                    nx, ny = i + dx, j + dy

                    if 1 <= nx < r + 1 and 1 <= ny < c + 1 and graph[nx][ny] != -1: # 좌표를 만족하는 경우
                        copy_graph[nx][ny] += dust
                        count += 1

                copy_graph[i][j] -= count * dust

    return copy_graph
    
def move(graph): # 미세먼지 이동
    copy_graph = copy.deepcopy(graph)

    # 왼쪽 이동
    copy_graph[mx - 1][2] = 0
    copy_graph[mx][2] = 0

    for i in range(3, c + 1):
        copy_graph[mx - 1][i] = graph[mx - 1][i - 1]
        copy_graph[mx][i] = graph[mx][i - 1]

    # 오른쪽 이동
    for i in range(c - 1, 0, -1):
        copy_graph[1][i] = graph[1][i + 1]
        copy_graph[r][i] = graph[r][i + 1]

    # 아래로 향하는 바람
    for i in range(2, r + 1):
        if i < mx - 1:
            copy_graph[i][1] = graph[i - 1][1]
        elif i > mx:
            copy_graph[i][c] = graph[i - 1][c]

    # 위로 향하는 바람
    for i in range(r - 1, 0, -1):
        if i > mx:
            copy_graph[i][1] = graph[i + 1][1]
        elif i < mx - 1:
            copy_graph[i][c] = graph[i + 1][c]

    return copy_graph


r, c, t = map(int, input().split())
graph = [[0 for _ in range(c + 2)] for _ in range(r + 2)]

for i in range(r):
    a = list(map(int, input().split()))

    for j in range(c):
        graph[i + 1][j + 1] = a[j]


mx, my = 0, 0   # 공기청정기 아래 좌표

# 공기청정기 좌표 구하기
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            mx, my = i, j

for _ in range(t):
    graph = spread(graph)
    graph = move(graph)
    

answer = 2
for i in range(1, r + 1):
    for j in range(1, c + 1):
        answer += graph[i][j]

print(answer)
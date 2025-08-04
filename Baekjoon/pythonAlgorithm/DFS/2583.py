# 영역 구하기, DFS를 사용하는 문제

import sys
sys.setrecursionlimit(1000000)

def DFS(y, x):
    global area

    if x < 0 or y < 0 or x >= N or y >= M:    # 좌표를 벗어나는 경우
        return False
    elif graph[y][x] == 1:  # 이미 방문을 한 경우
        return False
    else:
        graph[y][x] = 1
        area += 1

        DFS(y, x-1)
        DFS(y, x+1)
        DFS(y-1, x)
        DFS(y+1, x)


M, N, K = map(int, input().split()) # M은 y를, N은 x를 의미

graph = [[0 for _ in range(N)] for _ in range(M)]

# 직사각형 좌표 입력, 주어진 그림을 뒤집었다고 생각.
for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())  

    # 직사각형에 해당하는 부분 표시
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = 1

num_area = 0
answer_area = list()

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:    # 직사각형이 아닌 영역
            area = 0
            DFS(i, j)

            num_area += 1
            answer_area.append(area)

print(num_area)

answer_area.sort()
for i in answer_area:
    print(i, end=" ")
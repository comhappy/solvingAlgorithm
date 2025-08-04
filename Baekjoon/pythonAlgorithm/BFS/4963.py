# 섬의 개수

import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):  # 너비 우선 탐색은 queue를 통해서 함. x,y 는 시작 좌표
    bfsque = deque()
    bfsque.append([x, y])
    visited[x][y] = True

    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]    # 8방향 정의

    while(bfsque): # 큐가 빈 상태가 될때까지 반복
        x, y = bfsque.popleft()

        # 8방향 탐색
        for dx, dy in dxy:
            if 0 <= x + dx < h and 0 <= y + dy < w: # 좌표를 만족하는 경우
                if visited[x + dx][y + dy] == False and landsea[x + dx][y + dy] == 1:    # 방문하지 않은 땅인 경우
                    bfsque.append([x + dx, y + dy])
                    visited[x + dx][y + dy] = True

    return 1    


while(1):
    w, h = map(int, input().split())

    if w == 0 and h == 0:   # 0, 0이면 종료
        break
    else:
        visited = [[False for _ in range(w)] for _ in range(h)]
        landsea = list(list(map(int, input().split())) for _ in range(h))

        result = 0  # 섬의 개수

        for i in range(h):
            for j in range(w):
                if visited[i][j] == False and landsea[i][j] == 1:  # 방문하지 않은 땅에 대해서 BFS 실행
                    result += BFS(i, j)

        print(result)
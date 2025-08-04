# 토마토

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    que = deque()
    day = 1

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomato[i][j][k] == 1:    # 익은 토마토인 경우
                    que.append([i, j, k, day])

    while(que):
        i, j, k, day = que.popleft()

        # 6방향 조사
        for dx, dy, dz in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
            nz, ny, nx  = i + dx, j + dy, k + dz

            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n: # 좌표를 만족하는 경우
                if tomato[nz][ny][nx] == 0: # 익지 않은 토마토
                    tomato[nz][ny][nx] = day + 1
                    que.append([nz, ny, nx, day + 1])

    return day


def check_answer():
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomato[i][j][k] == 0:    # 익지않은 토마토인 경우
                    return 1  


n, m, h = map(int, input().split()) # y, x, z 순
tomato = list(list(list(map(int, input().split())) for _ in range(m)) for _ in range(h))

day = BFS()
check = check_answer()

if check:   # 익지않은 토마토 존재
    print(-1)
else:
    print(day - 1)
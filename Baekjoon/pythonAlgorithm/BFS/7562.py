# 나이트의 이동

from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx, sy, ex, ey):
    if sx == ex and sy == ey:   # 이동할 필요가 없을 때
        return 1

    depth = 1
    que = deque()
    que.append([sx, sy, depth])
    graph[sx][sy] = depth

    while(que):
        x, y, depth = que.popleft()

        for dx, dy in [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]:
            nx, ny = dx + x, dy + y     # 이동가능한 칸

            if 0 <= nx < l and 0 <= ny < l:     # 좌표를 만족
                if nx == ex and ny == ey:
                    return depth + 1

                if graph[nx][ny] == 0:  # 방문하지 않은 경우
                    que.append([nx, ny, depth + 1])
                    graph[nx][ny] = depth + 1

    return depth


t = int(input())

for _ in range(t):
    l = int(input())    # 체스판의 한 변의 길이
    sx, sy = map(int, input().split())  # 나이트가 현재 있는 칸
    ex, ey = map(int, input().split())  # 나이트가 이동하려고 하는 칸

    graph = [[0 for _ in range(l)] for _ in range(l)]

    answer = BFS(sx, sy, ex, ey)
    print(answer - 1)
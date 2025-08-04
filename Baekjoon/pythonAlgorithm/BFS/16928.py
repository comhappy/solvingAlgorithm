# 뱀과 사다리 게임

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    visited = [0 for _ in range(101)]   # 방문 여부
    count = 1   # 주사위를 던진 횟수

    que = deque()
    que.append([1, 0])
    visited[1] = 1

    while(que):
        point, count = que.popleft()

        if point == 100:
            print(count)
            break

        for i in range(point + 1, point + 7):   # 주사위를 굴려서 나올 수 있는 위치
            if 0 < i < 101 and visited[i] == 0: # 가능한 위치
                # 사다리를 통해 갈 수 있는 위치
                for x, y in ladder:
                    if x == i:
                        que.append([y, count + 1])
                        visited[x] = 1
                        visited[y] = 1
                
                # 뱀을 통해 갈 수 있는 위치
                for u, v in snake:
                    if u == i:
                        que.append([v, count + 1])
                        visited[u] = 1
                        visited[v] = 1

                if visited[i] == 0:
                    que.append([i, count + 1])
                    visited[i] = 1


n, m = map(int, input().split())

ladder = list()
snake = list()

for _ in range(n):
    x, y = map(int, input().split())
    ladder.append([x, y])

for _ in range(m):
    u, v = map(int, input().split())
    snake.append([u, v])

BFS()
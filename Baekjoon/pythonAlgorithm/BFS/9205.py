# 맥주 마시면서 걸어가기

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    que = deque()
    visited = [0 for _ in range(n + 2)]

    que.append(0)
    visited[0] = 1

    while(que):
        node = que.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1

    if visited[n + 1] == 1:
        print("happy")
    else:
        print("sad")


t = int(input())

store = list()

for _ in range(t):
    n = int(input())

    point = list()
    
    for _ in range(n + 2):
        x, y = map(int, input().split())
        point.append([x, y])

    graph = [[] for _ in range(n + 2)]

    for i in range(n + 2):
        sx, sy = point[i]

        for j in range(n + 2):
            ex, ey = point[j]

            if abs(sx - ex) + abs(sy - ey) != 0 and abs(sx - ex) + abs(sy - ey) <= 1000:
                graph[i].append(j)

    BFS()
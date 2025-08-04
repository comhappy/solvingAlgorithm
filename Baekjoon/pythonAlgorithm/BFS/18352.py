# 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline

def BFS(x):
    que = deque()
    visited = [0 for _ in range(n + 1)]

    que.append(x)
    visited[x] += 1

    while(que):
        start = que.popleft()

        for i in graph[start]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[start] + 1

    return visited

def check_answer(visited, k):
    if k + 1 not in visited:
        print(-1)
    else:
        for i in range(n + 1):
            if visited[i] == k + 1:
                print(i)


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

visited = BFS(x)
check_answer(visited, k)
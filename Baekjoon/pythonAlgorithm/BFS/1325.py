# 효율적인 해킹

from collections import deque

def BFS(number):
    que = deque()
    que.append(number)
    visited[number] = 1

    while(que):
        com = que.popleft()

        for i in graph[com]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[com] + 1
            else:
                visited[com] = visited[i] + 1


n, m = map(int, input().split())

graph = list(list() for _ in range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

visited = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if visited[i] == 0:
        BFS(i)

print(visited)
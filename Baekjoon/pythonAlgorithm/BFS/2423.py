# 전구를 켜라
# 회전하게 되면 1, 안하면 0

from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    que = deque()

    if graph[0][0] == "/": # 회전 해야함
        visited[0][0] = 1
        que.append([0, 0, "\\"])
    else:
        visited[0][0] = 0
        que.append([0, 0, "\\"])

    if graph[n - 1][m - 1] == "/": # 회전해야함
        graph[n - 1][m - 1] = "\\"
        visited[0][0] += 1

    while(que):
        x, y, state = que.popleft()

        if state == "\\":
            for dx, dy, dstate in [[-1, -1, "\\"], [-1, 0, "/"], [0, -1, "/"], [1, 1, "\\"], [1, 0, "/"], [0, 1, "/"]]:
                nx, ny = x + dx, y + dy

                if nx == n - 1 and ny == m - 1 and dstate == "/": # 탐색하는 좌표가 찾고자하는 좌표일 경우
                    continue

                if 0 <= nx < n and 0 <= ny < m and dstate == graph[nx][ny]: # 좌표를 만족, 변경이 불필요
                    if visited[nx][ny] > visited[x][y]:
                        que.appendleft([nx, ny, dstate])
                        visited[nx][ny] = visited[x][y]
                elif 0 <= nx < n and 0 <= ny < m and dstate != graph[nx][ny]:    # 변경이 필요
                    if visited[nx][ny] > visited[x][y] + 1:
                        que.append([nx, ny, dstate])
                        visited[nx][ny] = visited[x][y] + 1

        elif state == "/":
            for dx, dy, dstate in [[-1, 1, "/"], [-1, 0, "\\"], [0, 1, "\\"], [1, -1, "/"], [1, 0, "\\"], [0, -1, "\\"]]:
                nx, ny = x + dx, y + dy

                if nx == n - 1 and ny == m - 1 and dstate == "/": # 탐색하는 좌표가 찾고자하는 좌표일 경우
                    continue

                if 0 <= nx < n and 0 <= ny < m and dstate == graph[nx][ny]: # 좌표를 만족, 변경이 불필요
                    if visited[nx][ny] > visited[x][y]:
                        que.appendleft([nx, ny, dstate])
                        visited[nx][ny] = visited[x][y]
                elif 0 <= nx < n and 0 <= ny < m and dstate != graph[nx][ny]:    # 변경이 필요
                    if visited[nx][ny] > visited[x][y] + 1:
                        que.append([nx, ny, dstate])
                        visited[nx][ny] = visited[x][y] + 1


n, m = map(int, input().split())
graph = list(list(map(str, input().strip())) for _ in range(n))
visited = [[n * m for _ in range(m)] for _ in range(n)]

BFS()

if visited[n - 1][m - 1] == n * m:
    print("NO SOLUTION")
else:
    print(visited[n - 1][m - 1])
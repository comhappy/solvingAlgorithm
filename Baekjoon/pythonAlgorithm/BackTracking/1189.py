# 컴백홈

import sys
input = sys.stdin.readline

def DFS(x, y, depth):
    global answer

    if visited[x][y] == 1 or depth > k:  # 이미 방문한 경우
        return
    elif x == 0 and y == c - 1 and depth == k:  # 정답지에 도착한 경우
        answer += 1
        return
    else:
        visited[x][y] = 1


        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == ".":  # 이동할 수 있는 곳인 경우
                    DFS(nx, ny, depth + 1)
        
        visited[x][y] = 0

        return


r, c, k = map(int, input().split())
graph = list(list(i for i in input().strip()) for _ in range(r))

visited = [[0 for _ in range(c)] for _ in range(r)]
answer = 0

DFS(r - 1, 0, 1)
print(answer)
# 치즈

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    if visited[x][y] == 2:
        return
    
    if cheeze[x][y] == 0:   # 공기인 경우
        visited[x][y] = 2

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                DFS(nx, ny)

    elif cheeze[x][y] == 1: # 치즈인 경우
        visited[x][y] += 1

        if visited[x][y] == 2:
            cheeze[x][y] = 0

    return


def check_cheeze():
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                return 1
            
    return 0


n, m = map(int, input().split())
cheeze = list(list(map(int, input().split())) for _ in range(n))

t = 0
while(1):
    if check_cheeze() == 0:
        break

    visited = [[0 for _ in range(m)] for _ in range(n)]
    DFS(0, 0)
    t += 1

print(t)
# 치즈

import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):  # DFS를 사용하여 녹을 치즈 찾기
    if visited[x][y] == 1:
        return
    else:
        visited[x][y] = 1

        if cheeze[x][y] == 0:  # 공기인 경우
            for dx, dy in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m: # 좌표를 만족하는 경우
                    DFS(nx, ny)

        elif cheeze[x][y] == 1: # 치즈인 경우
            cheeze[x][y] = 0

def count_cheeze():
    count = 0

    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                count += 1

    return count


n, m = map(int, input().split())
cheeze = list(list(map(int, input().split())) for _ in range(n))
answer = [count_cheeze()]

while(1):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    DFS(0, 0)
    count = count_cheeze()

    answer.append(count)

    if count == 0:
        break

print(len(answer) - 1)
print(answer[len(answer) - 2])
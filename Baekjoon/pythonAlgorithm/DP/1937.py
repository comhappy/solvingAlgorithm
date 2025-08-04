# 욕심쟁이 판다

import sys
sys.setrecursionlimit(10**6)

def DP(x, y):
    if move[x][y] != -1:    # 방문한 경우
        return move[x][y]
    else:
        move[x][y] = 1
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if forest[x][y] > forest[nx][ny]:   # 사방에서 올 수 있는 경우
                    move[x][y] = max(move[x][y], DP(nx, ny) + 1)
        
        return move[x][y]


n = int(input())
forest = list(list(map(int, input().split())) for _ in range(n))
move = [[-1 for _ in range(n)] for _ in range(n)]    # 각 칸에서 이동할 수 있는 칸

for i in range(n):
    for j in range(n):
        DP(i, j)

answer = 0
for i in move:
    answer = max(max(i), answer)

print(answer)
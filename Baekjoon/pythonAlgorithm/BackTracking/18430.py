# 무기 공학
import sys
input = sys.stdin.readline

def check_xy(x, y): # x, y가 유효한 좌표인지 확인
    if 0 <= x < n and  0 <= y < m:
        if visited[x][y] == 0:
            return 1
    
    return 0

def DFS(xy, score):  # (x, y)를 중심으로 가지는 부매랑
    global answer

    x = xy // m
    y = xy % m

    if xy == n * m:
        answer = max(answer, score)
        return
    elif visited[x][y] == 1:
        DFS(xy + 1, score)
        return
    else:
        for ax, ay, bx, by in [[0, -1, 1, 0], [0, -1, -1, 0], [-1, 0, 0, 1], [1, 0, 0, 1]]:
            nax, nay, nbx, nby = x + ax, y + ay, x + bx, y + by

            if check_xy(nax, nay) and check_xy(nbx, nby):
                score += wood[x][y] * 2 + wood[nax][nay] + wood[nbx][nby]
                visited[nax][nay] = 1
                visited[nbx][nby] = 1
                visited[x][y] = 1

                DFS(xy + 1, score)

                score -= wood[x][y] * 2 + wood[nax][nay] + wood[nbx][nby]
                visited[nax][nay] = 0
                visited[nbx][nby] = 0
                visited[x][y] = 0
        DFS(xy + 1, score)


n, m = map(int, input().split())
wood = list(list(map(int, input().split())) for _ in range(n))
visited = [[0 for _ in range(m)] for _ in range(n)]
answer = 0

DFS(0, 0)

print(answer)
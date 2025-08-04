# 불!

from collections import deque

def BFS():
    que = deque()

    # 지훈이, 불 위치 찾기
    for i in range(r):
        for j in range(c):
            if miro[i][j] == "J":
                que.appendleft([i, j, 0])
            elif miro[i][j] == "F":
                que.append([i, j, 0])

    while(que):
        x, y, depth = que.popleft()

        if miro[x][y] == "J" and (x == 0 or y == 0 or x == r - 1 or y == c - 1):
            return depth + 1

        for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c :
                if miro[x][y] == "J" and miro[nx][ny] == ".":
                    que.append([nx, ny, depth + 1])
                    miro[nx][ny] = "J"

                if miro[x][y] == "F" and (miro[nx][ny] == "." or miro[nx][ny] == "J"):
                    que.append([nx, ny, depth + 1])
                    miro[nx][ny] = "F"

    return -1


r, c = map(int, input().split())
miro = list(list(i for i in input()) for _ in range(r))

answer = BFS()

if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer)
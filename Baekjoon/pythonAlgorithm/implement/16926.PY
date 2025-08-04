# 배열 돌리기

from collections import deque

def rotate(matrix):
    x, y, mx, ny = 0, 0, m - 1, n - 1

    while(1):
        if x > mx or y > ny:
            break

        rot = deque()

        # 원소 조회
        for i in range(y, ny + 1):  # 왼쪽 줄
            rot.append(matrix[i][x])

        for i in range(x + 1, mx + 1):  # 아래쪽 줄
            rot.append(matrix[ny][i])
        
        for i in range(ny - 1, y - 1, -1):  # 오른쪽 줄
            rot.append(matrix[i][mx])

        for i in range(mx - 1, x, -1):  # 윗쪽 줄
            rot.append(matrix[y][i])

        # 회전횟수에 따른 회전
        for _ in range(r % len(rot)):
            rot.appendleft(rot.pop())

        # 해당 위치에 원소 배정
        for i in range(y, ny + 1):  # 왼쪽 줄
            matrix[i][x] = rot.popleft()

        for i in range(x + 1, mx + 1):  # 아래쪽 줄
            matrix[ny][i] = rot.popleft()
        
        for i in range(ny - 1, y - 1, -1):  # 오른쪽 줄
            matrix[i][mx] = rot.popleft()

        for i in range(mx - 1, x, -1):  # 윗쪽 줄
            matrix[y][i] = rot.popleft()

        x, y, mx, ny = x + 1, y + 1, mx - 1, ny - 1

    return matrix


n, m, r = map(int, input().split())
matrix = list(list(map(int, input().split())) for _ in range(n))

matrix = rotate(matrix)

for i in matrix:
    print(*i)
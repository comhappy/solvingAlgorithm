# 로봇 청소기

import sys
input = sys.stdin.readline

def DFS(r, c, d):   # d의 값 = [0 북, 1 동, 2 남, 3 서]
    south = area[r + 1][c]
    north = area[r - 1][c]
    east = area[r][c + 1]
    west = area[r][c - 1]

    # 현재 칸이 청소되지 않은 경우, 현재 칸을 청소(상태는 2)
    if area[r][c] == 0:
        area[r][c] = 2

    # 주변 4개의 방향을 검사하는 경우
    if south == 0 or north == 0 or east == 0 or west == 0:  # 주변 4개의 칸 중 청소되지 않은 구역이 있는 경우
        d -= 1  # 반시계방향(북, 서, 남, 동 순으로 변화)

        if d < 0:
            d = 3

        # 청소되지 않은 경우
        if d == 0 and north == 0:  # 북쪽을 바라보는 경우
            DFS(r - 1, c, d)
        elif d == 1 and east == 0:    # 동쪽을 바라보는 경우
            DFS(r, c + 1, d)
        elif d == 2 and south == 0:    # 남쪽을 바라보는 경우
            DFS(r + 1, c, d)
        elif d == 3 and west == 0:    # 서쪽을 바라보는 경우
            DFS(r, c - 1, d)
        else:
            DFS(r, c, d)    # 돌아가는 경우
    
    else:   # 주변 4개의 칸이 청소되지 않은 칸이 없는 경우
        # 바라보는 방향을 유지한채로 후진 가능한 경우
        if d == 0:  # 북쪽을 바라보는 경우
            if area[r + 1][c] != 1: # 벽이 아닌 경우
                DFS(r + 1, c, d)
            else:
                return  # 벽인 경우
        elif d == 1:    # 동쪽을 바라보는 경우
            if area[r][c - 1] != 1:    
                DFS(r, c - 1, d)
            else:
                return
        elif d == 2:    # 남쪽을 바라보는 경우
            if area[r - 1][c] != 1:    
                DFS(r - 1, c, d)
            else:
                return
        elif d == 3:    # 서쪽을 바라보는 경우
            if area[r][c + 1] != 1:    
                DFS(r, c + 1, d)
            else:
                return


N, M = map(int, input().split())

r, c, d = map(int, input().split())     # r은 N, c는 M을 나타냄

area = list()

for _ in range(N):
    area.append(list(map(int, input().split())))

DFS(r, c, d)

ans = 0
for i in area:
    ans += i.count(2)

print(ans)
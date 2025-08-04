# 파이프 옮기기

import sys
input = sys.stdin.readline

def move(x, y, state):  # 이동 가능 여부 판별
    dxy1 = [[0, 1]] # 가로 확인
    dxy2 = [[1, 0]] # 세로 확인
    dxy3 = [[0, 1], [1, 0], [1, 1]] # 대각선 확인

    dfs = True

    if state == 1:
        dxy = dxy1
    elif state == 2:
        dxy = dxy2
    elif state == 3:
        dxy = dxy3

    for dx, dy in dxy:  # 이동여부
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if house[nx][ny] == 1:
                dfs = False
        else:   # 범위를 벗어나는 경우 이동 불가
            dfs = False
        
    return dfs

def DFS(x, y, state):
    global visited

    if x == n - 1 and y == n - 1:   # 목적지에 도착한 경우
        return 1
    if visited[state - 1][x][y] == 0:  # 방문하지 않은 경우

        if state == 1:  # 가로로 놓여진 경우
            if move(x, y, 1):   # 가로 이동 가능 여부
                visited[state - 1][x][y] += DFS(x, y + 1, 1)
                
            if move(x, y, 3):   # 대각선 이동 가능 여부
                visited[state - 1][x][y] += DFS(x + 1, y + 1, 3)
                
        elif state == 2:    # 세로로 놓여진 경우
            if move(x, y, 2):   # 세로 이동 가능 여부
                visited[state - 1][x][y] += DFS(x + 1, y, 2)
                
            if move(x, y, 3):   # 대각선 이동 가능 여부
                visited[state - 1][x][y] += DFS(x + 1, y + 1, 3)
               
        elif state == 3:    # 대각선으로 놓여진 경우
            if move(x, y, 1):   # 가로 이동 가능 여부
                visited[state - 1][x][y] += DFS(x, y + 1, 1)
            
            if move(x, y, 2):   # 세로 이동 가능 여부
                visited[state - 1][x][y] += DFS(x + 1, y, 2)
                
            if move(x, y, 3):   # 대각선 이동 가능 여부
                visited[state - 1][x][y] += DFS(x + 1, y + 1, 3)
    
    return visited[state - 1][x][y]
            

n = int(input())
house = list(list(map(int, input().split())) for _ in range(n))
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)] # 파이프 상태에 따른 경우의 수

if house[n - 1][n - 1] == 1:    # 도착지가 벽인 경우 가능한 경우는 없다
    print(0)
else:
    DFS(0, 1, 1)
    print(visited[0][0][1])
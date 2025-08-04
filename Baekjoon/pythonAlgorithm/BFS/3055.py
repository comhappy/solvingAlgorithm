# 탈출

from collections import deque
import sys
input = sys.stdin.readline

def checkmove(moveque, move, visited_moveque):  # 고슴도치가 존재가능한 좌표를 찾는 함수
    for _ in range(len(moveque)):
        x, y = moveque.popleft()

        if graph[x][y] == ".":  # 해당 위치가 땅인 경우에 이동 가능, 즉 물에 잠기지 않음

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:   # 4방향 탐색
                nx, ny = x + dx, y + dy

                if 0 <= nx < r and 0 <= ny < c and visited_moveque[nx][ny] == False: # 좌표를 만족하는 경우
                    if graph[nx][ny] == ".":    # 고슴도치가 이동가능한 경우
                        moveque.append([nx, ny])
                        visited_moveque[nx][ny] = True
                    elif graph[nx][ny] == "D":  # 도착지인 경우
                        print(move)
                        return 1, 1

    return moveque, visited_moveque

def BFS():
    que = deque()
    visited = [[0 for _ in range(c)] for _ in range(r)] # 물에 대한 BFS 검사
    moveque = deque()   # 고슴도치가 존재할 수 있는 위치
    visited_moveque = [[False for _ in range(c)] for _ in range(r)] # 고슴도치 이동여부
    depth = 1
    move = 1

    # 물이 있는 위치, 고슴도치 위치 탐색
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                que.append([i, j, depth])
                visited[i][j] = depth
            
            if graph[i][j] == "S":  # 비버의 시작 위치를 저장하고 땅으로 바꿔준다.
                sx, sy = i, j
                graph[i][j] = "."

    moveque.append([sx, sy])    # 고슴도치 위치
    visited_moveque[sx][sy] = True

    while(que or moveque):
        if que: # 물이 흘러갈 수있음
            x, y, depth = que.popleft()

            if depth == move:   # 초가 바뀔때마다 고슴도치의 이동 검사, move - 1 만큼 이동 가능
                moveque, visited_moveque = checkmove(moveque, move, visited_moveque)

                if moveque == 1:    # 정답인 경우
                    return
                elif len(moveque) == 0:   # 정답이 없는 경우, 도착지를 찾지 못하고 이동 불가능한 경우
                    print("KAKTUS")
                    return
                
                move += 1

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:   # 4방향 탐색
                nx, ny = x + dx, y + dy

                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == "." and visited[nx][ny] == 0:
                        graph[nx][ny] = "*"
                        que.append([nx, ny, depth + 1])
                        visited[nx][ny] = depth + 1
        
        else:   # 물이 흘러가지 못하지만 고슴도치는 이동할 수 있음
            moveque, visited_moveque = checkmove(moveque, move, visited_moveque)

            if moveque == 1:    # 정답인 경우
                return
            elif len(moveque) == 0:   # 정답이 없는 경우
                print("KAKTUS")
                return
            
            move += 1


r, c = map(int, input().split())
graph = list(list(map(str, list(input().strip()))) for _ in range(r))

BFS()
# 아기상어

from collections import deque

def BFS(sx, sy, size_baby):  # BFS를 통한 물고기 후보 구하기
    que = deque()
    fish_list = list()
    visited = [[False for _ in range(n)] for _ in range(n)]

    que.append([sx, sy, 1])
    visited[sx][sy] = True
    flag = 0    # 물고기 후보 결정시 변하는 flag

    while(que):
        x, y, dis = que.popleft()

        if flag != 0 and flag < dis:
            return dis, fish_list

        # 4방향 탐색
        for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n: # 좌표를 만족
                if visited[nx][ny] == False:    # 방문하지 않은 부분
                    if graph[nx][ny] == 0 or graph[nx][ny] == size_baby: # 통과가 되는 경우
                        que.append([nx, ny, dis + 1])   # 다음 탐색을 위해 queue에 추가
                        visited[nx][ny] = True

                    elif graph[nx][ny] < size_baby: # 물고기를 먹을 수 있는 경우
                        que.append([nx, ny, dis + 1])
                        fish_list.append([nx, ny])  # 물고기의 좌표 추가
                        visited[nx][ny] = True
                        flag = dis

    return 0, []


def check_fish(fish):   # 잡아먹을 물고기 좌표 반환
    fish_x = n
    fish_y = n

    for x, y in fish:
        if fish_x > x:  # x가 최소(제일 위에 있음)
            fish_x = x
            fish_y = y
        if fish_x == x:
            if fish_y > y:
                fish_x = x
                fish_y = y

        
    return fish_x, fish_y


def eat_fish(x, y, fish_x, fish_y): # 물고기 좌표 변환
    graph[fish_x][fish_y] = 9
    graph[x][y] = 0
    

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:    # 아기상어의 위치
            x = i
            y = j

time = 0
shark_size = 2
grow = shark_size

while(1):
    dis, fish_list = BFS(x, y, shark_size)

    if dis == 0:    # 종료 조건
        print(time)
        break
    else:   # 관련 변수 변경
        time += dis - 1
        fx, fy = check_fish(fish_list)
        eat_fish(x, y, fx, fy)
        x, y = fx, fy   # 좌표 변경
        
        # 고래 성장
        grow -= 1
        if grow == 0:
            if shark_size != 9:
                shark_size += 1
                grow = shark_size
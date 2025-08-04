# 청소년 상어

import copy

def move_fish():
    fish_num = 1
    copy_fish = copy.deepcopy(sort_fish)

    for x, y in copy_fish:  # 낮은 번호부터 접근
        while(1):
            dx, dy = ddir[dir[x][y]]    # 이동방향

            nx, ny = x + dx, y + dy

            if 0 <= nx < 4 and 0 <= ny < 4:               
                # 위치 정보 변경
                temp_x, temp_y = sort_fish[fish_num]
                sort_fish[fish_num] = sort_fish[fish[nx][ny]]
                sort_fish[fish[nx][ny]][0] = temp_x
                sort_fish[fish[nx][ny]][1] = temp_y
                # 위치 변경
                temp = fish[x][y]
                fish[x][y] = fish[nx][ny]
                fish[nx][ny] = temp

                # 방향 변경
                temp = dir[x][y]
                dir[x][y] = dir[nx][ny]
                dir[nx][ny] = temp

                break
            else:
                dir[x][y] += 1
        fish_num += 1



fish = [[0 for _ in range(4)] for _ in range(4)]
dir = [[0 for _ in range(4)] for _ in range(4)]
sort_fish = [[0, 0] for _ in range(17)]  # index번의 물고기의 위치를 저장하는 리스트
ddir = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]   # 이동방향

for i in range(4):
    info = list(map(int, input().split()))

    for j in range(4):
        fish[i][j] = info[j * 2]
        dir[i][j] = info[j * 2 + 1]

        sort_fish[info[j * 2]][0] = i
        sort_fish[info[j * 2]][1] = j

for i in dir:
    print(i)


move_fish()

for i in fish:
    print(i)
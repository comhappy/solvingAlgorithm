# 감시

def CCTV_right(x, y, copy_office):
    y += 1
    while(y < M):  # 오른쪽 끝까지
        if copy_office[x][y] == 0:  # 비어있는 경우
            copy_office[x][y] = "#"
        elif copy_office[x][y] == 6:    # 벽인 경우
            break

        # CCTV를 만나는 경우는 지나감

        y += 1

def CCTV_left(x, y, copy_office):
    y -= 1
    while(y >= 0):  # 왼쪽 끝까지
        if copy_office[x][y] == 0:  # 비어있는 경우
            copy_office[x][y] = "#"
        elif copy_office[x][y] == 6:    # 벽인 경우
            break

        # CCTV를 만나는 경우는 지나감

        y -= 1

def CCTV_up(x, y, copy_office):
    x -= 1
    while(x >= 0):  # 위쪽 끝까지
        if copy_office[x][y] == 0:  # 비어있는 경우
            copy_office[x][y] = "#"
        elif copy_office[x][y] == 6:    # 벽인 경우
            break

        # CCTV를 만나는 경우는 지나감

        x -= 1

def CCTV_down(x, y, copy_office):
    x += 1
    while(x < N):  # 아래쪽 끝까지
        if copy_office[x][y] == 0:  # 비어있는 경우
            copy_office[x][y] = "#"
        elif copy_office[x][y] == 6:    # 벽인 경우
            break

        # CCTV를 만나는 경우는 지나감

        x += 1

import copy

def cal_area():
    # 사무실 복사본 만들기

    # 얕은 복사 방법
    #copy_office = list()
    # for i in office:
    #     copy_office.append(i)

    # 깊은 복사 방법 1
    copy_office = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_office[i][j] = office[i][j]

    # 깊은 복사 방법 2(2차원 이상의 리스트는 얕은복사가 된다.)
    # copy_office = office.copy()

    # 깊은 복사 방법 3
    # copy_office = copy.deepcopy(office)

    # 조건에 따른 감시영역 계산
    for i in range(len(order_of_CCTV)):
        num = order_of_CCTV[i]
        x, y = loc_of_CCTV[i]
        state = state_of_CCTV[i]

        if num == 1:
            if state == 1:
                CCTV_right(x, y, copy_office)
            elif state == 2:
                CCTV_down(x, y, copy_office)
            elif state == 3:
                CCTV_left(x, y, copy_office)
            elif state == 4:
                CCTV_up(x, y, copy_office)

        elif num == 2:
            if state == 1:
                CCTV_right(x, y, copy_office)
                CCTV_left(x, y, copy_office)
            elif state == 2:
                CCTV_up(x, y, copy_office)
                CCTV_down(x, y, copy_office)

        elif num == 3:
            if state == 1:
                CCTV_up(x, y, copy_office)
                CCTV_right(x, y, copy_office)
            elif state == 2:
                CCTV_right(x, y, copy_office)
                CCTV_down(x, y, copy_office)
            elif state == 3:
                CCTV_down(x, y, copy_office)
                CCTV_left(x, y, copy_office)
            elif state == 4:
                CCTV_left(x, y, copy_office)
                CCTV_up(x, y, copy_office)

        elif num == 4:
            if state == 1:
                CCTV_right(x, y, copy_office)
                CCTV_down(x, y, copy_office)
                CCTV_left(x, y, copy_office)

            elif state == 2:
                CCTV_down(x, y, copy_office)
                CCTV_left(x, y, copy_office)
                CCTV_up(x, y, copy_office)

            elif state == 3:
                CCTV_left(x, y, copy_office)
                CCTV_up(x, y, copy_office)
                CCTV_right(x, y, copy_office)

            elif state == 4:
                CCTV_up(x, y, copy_office)
                CCTV_right(x, y, copy_office)
                CCTV_down(x, y, copy_office)

        elif num == 5:
            CCTV_right(x, y, copy_office)
            CCTV_down(x, y, copy_office)
            CCTV_left(x, y, copy_office)
            CCTV_up(x, y, copy_office)

    # 사각지대 계산
    global min_result
    result = 0

    

    for i in range(N):
        for j in range(M):
            if copy_office[i][j] == 0:
                result += 1

    # 최솟값 결정
    if result < min_result:
        min_result = result


def DFS(depth):
    if len(state_of_CCTV) == len(order_of_CCTV):
        cal_area()  # 감시영역 계산

    else:
        # CCTV의 숫자가 1, 3, 4인 경우(가능한 종류가 4가지)
        if order_of_CCTV[depth] == 1 or order_of_CCTV[depth] == 3 or order_of_CCTV[depth] == 4:
            for i in range(1, 5):   # 1 ~ 4 종류 탐색
                state_of_CCTV.append(i)
                DFS(depth + 1)
                state_of_CCTV.pop()

        elif order_of_CCTV[depth] == 2:
            for i in range(1, 3):   # 1 ~ 2 종류 탐색
                state_of_CCTV.append(i)
                DFS(depth + 1)
                state_of_CCTV.pop()

        elif order_of_CCTV[depth] == 5:
            # 1종류 탐색
            state_of_CCTV.append(1)
            DFS(depth + 1)
            state_of_CCTV.pop()



N, M = map(int, input().split())    # 세로, 가로
office = list() # 사무실을 나타내는 배열

for _ in range(N):
    office.append(list(map(int, input().split())))

order_of_CCTV = list()  # 순서대로 나타나는 CCTV의 번호
loc_of_CCTV = list()    # 순서대로 나타나는 CCTV의 좌표
state_of_CCTV = list()  # 순서대로 나타나는 CCTV의 상태

min_result = 0

# CCTV 정보관리
for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:  # 빈자리, 벽이 아닌 경우
            order_of_CCTV.append(office[i][j])  # CCTV의 종류와 위치를 저장
            loc_of_CCTV.append([i, j])
        min_result += 1

DFS(0)  # DFS를 통한 CCTV 상태 검사

print(min_result)
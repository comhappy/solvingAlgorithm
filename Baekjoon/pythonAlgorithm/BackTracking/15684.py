# 사다리 조작

import sys
input = sys.stdin.readline

def appendladder(x, y):
    for i in range(-1, 2):
        if y + i >= 0 and y + i < N - 1:
            if i == 0:
                ladder[x][y + i] = 1
            else:
                ladder[x][y + i] = 2

def popladder(x, y):    # 1, 2
    ladder[x][y] = 0    # 가운데 부분 변경

    # 왼쪽 부분 변경
    if (y - 2) >= 0:    # 왼쪽 부분을 변경하지 말하야할 경우
        if ladder[x][y - 2] == 1:
            ladder[x][y - 1] = 2
        else:
            ladder[x][y - 1] = 0
    elif (y - 1) >= 0:
        ladder[x][y - 1] = 0

    # 오른쪽 부분 변경
    if (y + 2) < N - 1:    # 오른쪽 부분을 변경하지 말하야할 경우
        if ladder[x][y + 2] == 1:
            ladder[x][y + 1] = 2
        else:
            ladder[x][y + 1] = 0
    elif (y + 1) < N - 1:
        ladder[x][y + 1] = 0


def checkladder(start):
    x = 0   # 위치를 나타내는 x, y
    y = start
    
    while(x != H):    # 가로로 도달하는 경우 종료
        if y == 0:  # 가장 왼쪽에 위치하는 경우, 오른쪽의 사다리 유무만 보면됨
            if ladder[x][0] == 1:
                y += 1
                x += 1
            else:
                x += 1
        elif y == N - 1:    # 가장 오른쪽에 위치하는 경우, 왼쪽의 사다리 유무만 보면됨
            if ladder[x][N - 2] == 1:
                y -= 1
                x += 1
            else:
                x += 1
        else:  # 가운데 있는 경우
            if ladder[x][y] == 1:   # 왼쪽 가로 사다리가 존재하는 경우
                y += 1
                x += 1
            elif ladder[x][y - 1] == 1: # 오른쪽 가로 사다리가 존재하는 경우
                y -= 1
                x += 1
            else:   # 둘다 없는 경우
                x += 1

    if start == y:
        return True
    else:
        return False


def DFS(depth, index):
    global result

    # if depth == 4:  # 정답이 3보다 큰 값인 경우(4이상인 경우)
    #     # print("4 이상인 경우")   # 정답은 -1
    #     return
    # else:

    # 검사
    checkanswer = 0

    for i in range(N):  # 0 ~ (N-1) 까지 검사
        if checkladder(i):
            checkanswer += 1
            continue
        else:
            break

    
    if checkanswer == N:    # 정답을 만족함
        result.append(depth)
        return
    
    else:   # 정답을 만족하지 않음, 사다리 추가
        for i in range(index, (N - 1) * H):    # for i in range((N - 1) * H) 이렇게 표시한다면 순열의 의미.
            x = i // (N - 1)
            y = i % (N - 1)

            if ladder[x][y] == 0 and (depth + 1) <= 3:   # 사다리를 추가가능한 경우
                appendladder(x, y)
                DFS(depth + 1, i)
                popladder(x, y)


N, M, H = map(int, input().split()) # 세로선 N, 가로선 M

# 사다리 상태 리스트(1 연결, 2 설치불가, 0 설치가능)
ladder = [[0 for _ in range(N - 1)] for _ in range(H)]

# 가로선 추가, 추가 가능 여부 체크
for _ in range(M):
    a, b = map(int, input().split())

    appendladder(a - 1, b - 1)
    
result = list()

DFS(0, 0)

if result == []:
    print(-1)
else:
    print(min(result))
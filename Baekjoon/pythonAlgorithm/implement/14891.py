# 톱니바퀴

from collections import deque

def dfs_check(n, d):    # 회전해야하는 바퀴, 방향 저장
    if visited[n] == 1:
        return
    else:
        visited[n] = 1
        ro.append([n, d])

        if n + 1 < 5:
            if wheel[n][2] != wheel[n + 1][6]:  # 회전해야하는 경우
                dfs_check(n + 1, d * -1)
        if n - 1 > 0:
            if wheel[n][6] != wheel[n - 1][2]:  # 회전해야하는 경우
                dfs_check(n - 1, d * -1)

        return


def rotate(n, d):   # 바퀴를 회전
    if d == 1:  # 시계방향 회전
        a = wheel[n].pop()
        wheel[n].appendleft(a)

    elif d == -1:   # 반시계방향 회전
        a = wheel[n].popleft()
        wheel[n].append(a)


wheel = [deque() for _ in range(5)]

# 바퀴 상태
for i in range(1, 5):
    for j in input():
        wheel[i].append(int(j))

# 회전 횟수
k = int(input())

for _ in range(k):
    # 맞닿아 있는 부분 검사 -> 회전 바퀴 결정 -> 회전
    n, d = map(int, input().split())    # 회전을 시작하는 바퀴, 방향

    visited = [0 for _ in range(5)] # 방문체크
    ro = [[0, 0]]   # 회전해야하는 바퀴, 방향

    dfs_check(n, d)

    # 바퀴 회전
    for a, b in ro:
        rotate(a, b)
    
answer = 0

for i in range(1, 5):
    if wheel[i][0] == 1:
        answer += 2 ** (i - 1)

print(answer)
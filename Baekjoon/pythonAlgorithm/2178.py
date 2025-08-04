# 미로 탐색~

from collections import deque

def check_queueinsert(x, y):
    if x < 0 or y < 0 or x > N - 1 or y > M - 1:    # 미로 외각의 값을 가질 때
        return False

    if (visited_A[x][y] == False) and (A[x][y] == 1):     # 방문할 수 있는 칸
        return True
    else:
        return False

# BFS를 시작 후, 깊이를 추적함.
# depth에 해당하는 노드를 queue에 삽입 후 처리, 이후 다른 queue로 처리해 줌

def BFS_miro(x, y):
    BFS_queue = deque()
    BFS_queue.append([x, y])
    visited_A[x][y] = True

    px, py = x, y
    depth = 0

    BFS_queue_before = deque()

    while((px == N - 1 and py == M - 1) == False):
        depth += 1

        # queue가 비어있을 때까지 반복
        while BFS_queue:
            px, py = BFS_queue.popleft()    # 현재 위치
            if (px == N - 1) and (py == M - 1): # 종료조건
                break

            # 인접한 위치에 접근 가능한지 확인
            if check_queueinsert(px - 1, py):    # 위쪽
                    BFS_queue_before.append([px - 1, py])
                    visited_A[px - 1][py] = True

            if check_queueinsert(px + 1, py):    # 아래쪽
                BFS_queue_before.append([px + 1, py])
                visited_A[px + 1][py] = True

            if check_queueinsert(px, py - 1):    # 왼쪽
                BFS_queue_before.append([px, py - 1])
                visited_A[px][py - 1] = True

            if check_queueinsert(px, py + 1):    # 오른쪽
                BFS_queue_before.append([px, py + 1])
                visited_A[px][py + 1] = True

        # queue 복사 및 초기화
        BFS_queue = BFS_queue_before.copy()
        BFS_queue_before.clear()

    return depth


N, M = map(int, input().split())

# 2차원 배열로 미로 표현하기
A = []
visited_A = [[False for _ in range(M)] for _ in range(N)] 

for i in range(N):
    v = list()
    for j in input():
        v.append(int(j))
    A.append(v)

print(BFS_miro(0, 0))
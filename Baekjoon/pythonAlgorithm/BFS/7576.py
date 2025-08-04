# 토마토

from collections import deque
import sys
input = sys.stdin.readline

def BFS(tomato):
    que = deque()

    # 시작점 찾기, 병렬로 토마토가 익어가야하므로 시작점을 찾아준다.
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                que.append([i,j])

    while(que):
        i, j = que.popleft()

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:   # 4방향 검사
            nx = i + dx
            ny = j + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if tomato[nx][ny] == 0: # 익지 않은 토마토
                    tomato[nx][ny] = tomato[i][j] + 1   # 현재 상태 + 1
                    que.append([nx, ny])

# 배열을 순회하면서 0이 있으면 -1을 리턴, 없으면 최댓값 - 1을 리턴
def get_answer(tomato):
    answer = -1

    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                answer = -1
                return answer
            elif tomato[i][j] > answer:
                answer = tomato[i][j] - 1

    return answer


m, n = map(int, input().split())
tomato = list(list(map(int, input().split())) for _ in range(n))

BFS(tomato)
print(get_answer(tomato))
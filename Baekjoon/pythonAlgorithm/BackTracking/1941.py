# 소문난 칠공주
# 25명 중 7명을 뽑는 문제. 조건(7명 중 4명 이상이 이다솜파이다. 7명은 근접해있어야한다.)

from collections import deque
import copy

def BFS(i, j):
    count = 0
    copy_visited = copy.deepcopy(visited)
    
    que = deque()
    que.append([i, j])
    copy_visited[i][j] = 0
    

    while(que):
        x, y = que.popleft()
        count += 1

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 5 and 0 <= ny < 5:
                if copy_visited[nx][ny] == 1:
                    que.append([nx, ny])
                    copy_visited[nx][ny] = 0
    
    if count == 7:
        return True
    else:
        return False


def DFS(n, depth, sp, yp):
    global answer

    if yp >= 4:
        return
    elif depth == 7:  # 7명을 전부 뽑은 경우
        # 붙어있는지 검사
        for i in range(5):
            for j in range(5):
                if visited[i][j] == 1:
                    if BFS(i, j):
                        answer += 1
                    return
    else:
        for i in range(n ,25):
            x = i % 5
            y = i // 5

            if visited[x][y] == 0:
                visited[x][y] = 1

                if SY[x][y] == "S":
                    DFS(i, depth + 1, sp + 1, yp)
                else:
                    DFS(i, depth + 1, sp, yp + 1)

                visited[x][y] = 0


SY = list()

for _ in range(5):
    SY.append(list(input()))

answer = 0
visited = [[0 for _ in range(5)] for _ in range(5)]

DFS(0, 0, 0, 0)

print(answer)
# 벽 부수고 이동하기
# BFS는 각각의 상황에서 최단거리를 보장한다. 이 특성을 이용해서 벽을 부순 상황과 벽을 부수지 않은 상황을 한번에 탐색한다.
# 벽을 부수지 않은 상황(visited[0][x][y])에서는 벽을 부순 상황(visited[1][x][y])으로 갈 수있다.
# 벽을 부순 상황(visited[1][x][y])에서는 오직 벽을 부순 상황(visited[1][x][y])으로 갈 수있다.
# 정리하면 0에서는 0, 1로 이동이 가능하지만 1에서는 오직 1로 이동 가능하다. 이러한 상황을 아래 코드에 작성하였다.


from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    que = deque()
    que.append([0, 0, 0])   # 초기상태는 벽을 뚫지 않음, 좌표는 0, 0
    visited[0][0][0] = 1    # 방문 여부 체크
    visited[1][0][0] = 1

    while(que):
        wall, x, y = que.popleft()  # 벽뚫 여부, 좌표 : 이 상황을 이용해 위에 정리한 이동 가능성을 확인하는 것

        for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:   # 4방향 탐색
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m: # 좌표를 만족
                if wall == 0:   # 0>0, 0>1 가능
                    if graph[nx][ny] == 0 and visited[0][nx][ny] == 0:  # 벽을 뚫지않고, 방문 가능한 경우
                        visited[0][nx][ny] = visited[0][x][y] + 1
                        que.append([0, nx, ny])
                    elif graph[nx][ny] == 1 and visited[1][nx][ny] == 0:    # 벽을 뚫은 경우, 방문 가능한 경우
                        visited[1][nx][ny] = visited[0][x][y] + 1
                        que.append([1, nx, ny])


                elif wall == 1: # 1 > 1 가능
                    if graph[nx][ny] == 0 and visited[1][nx][ny] == 0:  # 벽을 뚫지않고, 방문 가능한 경우
                        visited[1][nx][ny] = visited[1][x][y] + 1
                        que.append([1, nx, ny])


                if wall == 0 and graph[nx][ny] == 1 and visited[1][nx][ny] == 0:  # 벽인 경우 벽을 뚫지 않아야한다. 벽을 뚫은 visited 배열을 본다.
                    # 벽을 뚫는 경우, 0 > 1 의 세상만 만족
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    que.append([1, nx, ny])

                elif graph[nx][ny] == 0 and visited[wall][nx][ny] == 0:    # 벽이 아닌 경우, 벽을 뚫지 않은 visited 배열을 본다.
                    visited[wall][nx][ny] = visited[wall][x][y] + 1
                    que.append([wall, nx, ny])

    answer1 = visited[0][n - 1][m - 1]
    answer2 = visited[1][n - 1][m - 1]

    if answer1 == 0 and answer2 == 0:   # 안되는 경우
        return -1
    elif answer1 == 0:
        return answer2
    elif answer2 == 0:
        return answer1
    else:
        return min(answer1, answer2)


# n, m, 지도 입력
n, m = map(int, input().split())
graph = list(list(map(int, list(input().strip()))) for _ in range(n))
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)] # 벽 상태에 따른 방문여부를 나타내기 위한 3차원 배열

print(BFS())
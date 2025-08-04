# 적록색약

from collections import deque
import sys
input = sys.stdin.readline

def BFS_RGB(x, y, area_num):    # 구역을 찾아주는 BFS
    if visited[x][y] == 0:  # 방문하지 않은 경우
        que = deque()
        que.append([x, y])
        visited[x][y] = area_num

        while(que):
            x, y = que.popleft()

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + dx, y + dy # 확인할 좌표
                
                if 0 <= nx < n and 0 <= ny < n: # 좌표를 만족하는 경우
                    if visited[nx][ny] == 0 and RGB[nx][ny] == RGB[x][y]:   # 방문하지 않았고 색이 같은 경우
                        visited[nx][ny] = visited[x][y]
                        que.append([nx, ny])    # 다음에 탐색


n = int(input())    
RGB = list(list(map(str, input().strip())) for _ in range(n))   # RGB 정보를 담는 2차원 리스트
visited = [[0 for _ in range(n)] for _ in range(n)]

# 적록색맹이 아닌 사람의 구역 구하기
area_num = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            BFS_RGB(i, j, area_num)
            area_num += 1

print(area_num - 1, end=' ')

# 적록색맹인 사람의 구역 구하기

# 색 변경
for i in range(n):
    for j in range(n):
        if RGB[i][j] == 'R':
            RGB[i][j] = 'G'

# 관련 변수 초기화
visited = [[0 for _ in range(n)] for _ in range(n)]
area_num = 1

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            BFS_RGB(i, j, area_num)
            area_num += 1

print(area_num - 1)
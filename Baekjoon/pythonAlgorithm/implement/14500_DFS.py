# 테트로미노
# DFS를 사용해서 문제를 풀어보자

# DFS를 이용해서 블럭 4개를 선택, ㅗ 모양은 고려하지 못함
def DFS(x, y):
    global max_sum

    if x >= 0 and x < N and y >=0 and y < M:  # 좌표를 만족
        if visited[x][y] == False:  # 방문하지 않은 경우
            point.append([x, y])
            visited[x][y] = True

            if len(point) == 4:
                # 최댓값 계산
                sum_point = 0
                for px, py in point:
                    sum_point += paper[px][py]

                if sum_point > max_sum:
                    max_sum = sum_point
            else:
                DFS(x, y - 1)   # 좌
                DFS(x, y + 1)   # 우
                DFS(x - 1, y)   # 위
                DFS(x + 1, y)   # 아래

            point.pop()
            visited[x][y] = False

def tetromino():    # ㅗ 모양을 고려하는 함수, 중앙 좌표를 기준으로 검사할것임.
    global max_sum

    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 테두리를 제외한 부분 검사    
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            point_5 = paper[x][y] + paper[x + 1][y] + paper[x - 1][y] + paper[x][y + 1] + paper[x][y - 1]

            for i, j in dxy:
                sum_point = point_5 - paper[x + i][y + j]

                if sum_point > max_sum:
                    max_sum = sum_point

    
    for y in range(1, M - 1):   # 윗 줄
        sum_point =  paper[0][y - 1] + paper[0][y] + paper[0][y + 1] + paper[1][y]

        if sum_point > max_sum:
            max_sum = sum_point

    for x in range(1, N - 1):    # 왼쪽 줄
        sum_point =  paper[x - 1][0] + paper[x][0] + paper[x + 1][0] + paper[x][1]

        if sum_point > max_sum:
            max_sum = sum_point

    for y in range(1, M - 1):    # 아래쪽 줄
        sum_point =  paper[N - 1][y - 1] + paper[N - 1][y] + paper[N - 1][y + 1] + paper[N - 2][y]

        if sum_point > max_sum:
            max_sum = sum_point

    for x in range(1, N - 1):    # 오른쪽 줄
        sum_point =  paper[x - 1][M - 1] + paper[x][M - 1] + paper[x + 1][M - 1] + paper[x][M - 2]

        if sum_point > max_sum:
            max_sum = sum_point



import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))

visited = [[False for _ in range(M)] for _ in range(N)] # 방문여부를 나타내는 리스트    
point = list()  # 테트로미노를 나타내는 좌표들의 집합

max_sum = 0

for i in range(N):  # 시작점이 i, j이면서 테트로미노를 만들 수 있는 경우를 모두 탐색
    for j in range(M):
        DFS(i, j)

tetromino()

print(max_sum)
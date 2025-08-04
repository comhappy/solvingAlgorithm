# 인구 이동

from collections import deque
import sys
input = sys.stdin.readline

def BFS(n, l, r, graph):  # BFS를 이용해 연합을 구함
    que = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    update_people = list()  # 국경에 대한 갱신값을 저장하는 리스트
    day = 0

    while(1):
        # 연합 구하기
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:  # 방문하지 않았다면 탐색
                    que.append([i, j]) # 좌표
                    visited[i][j] = num
                    update_flag = False # 갱신되지 않는 국가(크기가 1인 국가)를 확인하기 위한 변수

                    num_of_con = 1
                    sum_of_con = graph[i][j]

                    while(que):
                        x, y = que.popleft()

                        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            nx, ny = dx + x, dy + y
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:   # 좌표를 만족하는 경우
                                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:  # 연합의 조건
                                    que.append([nx, ny])
                                    visited[nx][ny] = num
                                    update_flag = True  # 국가가 연합했으므로 flag를 바꿔줌

                                    num_of_con += 1
                                    sum_of_con += graph[nx][ny]
                    if update_flag: # 2개 이상 연합국에 대해서 변경
                        update_people.append([num, num_of_con, sum_of_con])
                    
                    num += 1    # 연합 숫자 증가

        # 탈출조건 : 국경이 update 되지 않음. 즉, 국가가 모두 1개로 이루어짐
        if len(update_people) == 0:
            break

        # 연합의 인구수 조정
        for contry, num_of_con, sum_of_con in update_people:
            for i in range(n):
                for j in range(n):
                    if visited[i][j] == contry:
                        graph[i][j] = int(sum_of_con / num_of_con)

        day += 1

        # 관련 변수 초기화
        visited = [[0 for _ in range(n)] for _ in range(n)]
        update_people = list()

    return day


n, l, r = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

print(BFS(n, l, r, graph))
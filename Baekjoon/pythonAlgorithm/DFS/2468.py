# 안전영역, DFS를 사용하는 문제
# 안전영역이 최대로 몇개가 만들어 지는지 확인

import sys
sys.setrecursionlimit(1000000)

def DFS(x, y):
    if x < 0 or y < 0 or x > (N - 1) or y > (N - 1):  # 좌표 이탈
        return False
    elif graph_copy[x][y] < 1:  # 잠김, DFS 안해도됨
        return False
    else:
        graph_copy[x][y] = 0    # 도착했다는 것을 알림

        DFS(x, y-1)
        DFS(x, y+1)
        DFS(x-1, y)
        DFS(x+1, y)
           
    
N = int(input())

# graph 만들기, 가장 높은 높이 구하기
graph = list()
maxheight = 0

for i in range(N):
    h = list(map(int, input().split()))
    graph.append(h)

    mh = max(h)

    if maxheight < mh:
        maxheight = mh

answer = list()
graph_copy = [[0 for i in range(N)] for j in range(N)]

for rain in range(maxheight + 1):
    # 지역 높이 - 물의 높이
    for i in range(N):
        for j in range(N):
            graph_copy[i][j] = graph[i][j] - rain

    # DFS로 안전지역 구하기
    safearea = 0

    for i in range(N):
        for j in range(N):
            if graph_copy[i][j] > 0:
                DFS(i, j)
                safearea += 1

    answer.append(safearea)
    
print(max(answer))
# 이분 그래프
# 이분 그래프란 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
# 즉 그래프 탐색을 통해서 두 가지 색상으로 나타낼 수 있는지 확인

from collections import deque
import sys
input = sys.stdin.readline

def BFS(vertex):
    color = 1
    que = deque()
    que.append([vertex, color])
    
    visited[vertex] = color     # 처음 노드를 1로 칠함

    while(que):
        node, color = que.popleft()
        
        # 1 or 2 의 값을 가지도록 함.
        if color == 1:
            color = 2
        elif color == 2:
            color = 1

        for i in graph[node]:
            if visited[i] == 0:
                que.append([i, color])
                visited[i] = color


def check_BG(graph, visited):
    for i in range(v + 1):
        for j in graph[i]:
            if visited[i] == visited[j]: # 인접한 노드가 같은 색상인 상황
                return "NO"
            
    return "YES"


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]

    # 무방향 그래프 생성
    for _ in range(e):
        num1, num2 = map(int, input().split())  
        graph[num1].append(num2)
        graph[num2].append(num1)

    # 전체 그래프에 대헤서 BFS
    for i in range(1, v + 1):
        if visited[i] == 0:     # 방문하지 않았을 경우
            BFS(i)
    
    answer = check_BG(graph, visited)
    print(answer)
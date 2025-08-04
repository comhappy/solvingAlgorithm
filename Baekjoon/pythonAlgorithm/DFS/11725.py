# 트리의 부모 찾기, DFS를 사용하는 문제
# 무방향 연결그래프로 트리 구성, DFS하면서 각각에 노드에 해당하는 부모를 리스트에 저장

import sys
sys.setrecursionlimit(1000000)

# def DFS(node):
#     global answer

#     if visited[node] == True:   # 방문했을 경우
#         return False
#     else:
#         visited[node] = True
#         for i in graph[node]:   # 연결된 노드(자식, 부모 모두 포함)
#             if visited[i] == True: # 노드를 방문했다는 뜻
#                 continue
#             else:           # 방문하지 않은 노드를 DFS
#                 answer[i] = node    
#                 DFS(i)
#         return True
    
def DFS(node):
    global answer   #  global 변수는 시간을 많이 잡아먹는 원인이 된다.

    visited[node] = True
    for i in graph[node]:   # 연결된 노드(자식, 부모 모두 포함)
        if visited[i] == False: # 방문하지 않은 노드에 대해서(자식노드)
            answer[i] = node    
            DFS(i)
    return True


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)

# 무방향 연결그래프
for i in range(N - 1):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

DFS(1)

for i in range(2, N + 1):
    print(answer[i])
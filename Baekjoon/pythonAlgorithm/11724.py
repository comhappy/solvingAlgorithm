# 무방향 그래프가 주어졌을 때, 연결요소 개수를 구하는 문제. 연결요소는 노드끼리 연결되어 있는 묶음의 개수
# 즉 그래프의 전체적인 탐색이 필요
# 인접 리스트를 활용해서 그래프를 표현

import sys
sys.setrecursionlimit(10000)    # 백준 온라인 저지의 기본 recursionlimit은 1000이므로 설정을 해주어야함

N, M = map(int, sys.stdin.readline().split())

#인접리스트를 활용하여 무방향 그래프 표현
G = [[] for _ in range(N + 1)]
visitedG = [False] * (N + 1)


def DFS(v):
    visitedG[v] = True  # vertex(노드)를 방문했다고 표시

    for i in G[v]:
        if visitedG[i] == False: # vertex(노드)를 방문하지 않았다면
            DFS(i)


for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    G[s].append(e)
    G[e].append(s)

#DFS 실행, DFS의 실행횟수가 연결요소의 개수
result = 0

for i in range(1, N+1):
    if visitedG[i] == False:
        DFS(i)
        result += 1


print(result)
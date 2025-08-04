# 무방향 그래프가 주어졌을 때, 연결요소 개수를 구하는 문제. 연결요소는 노드끼리 연결되어 있는 묶음의 개수
# 즉 그래프의 전체적인 탐색이 필요
# 인접 리스트를 활용해서 그래프를 표현

import sys
sys.setrecursionlimit(10000)    # 백준 온라인 저지의 기본 recursionlimit은 1000이므로 설정을 해주어야함

#DFS 구현
def DFS(node):
    if Avisted[node] == True:   # 방문한 경우
        return
    else:   # 방문하지 않은 경우
        Avisted[node] = True
        print("{} 방문".format(node), end="  ")

        for i in Alist[node]:
            DFS(i)

N, M = map(int, sys.stdin.readline().split())

#방문리스트 구현
Avisted = [False] * (N + 1)

#인접리스트를 활용하여 무방향 그래프 표현
Alist = [[] for _ in range(N + 1)]

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    Alist[node1].append(node2)
    Alist[node2].append(node1)

# 정답구하기
result = 0

for i in range(1, N):
    if Avisted[i] == False:
        DFS(i)
        print()
        result += 1

print(result)
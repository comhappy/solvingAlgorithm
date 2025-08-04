# 트리와 쿼리

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(n):
    # 이미 방문한 경우
    if visited[n] == 1:
        return 0

    visited[n] = 1  # 방문처리

    for i in graph[n]:
        dp[n] += DFS(i)

    return dp[n]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[v].append(u)
    graph[u].append(v)

dp = [1 for _ in range(n + 1)]  # i번째 정점을 루트라고 했을때 정점의 수
visited = [0 for _ in range(n + 1)]
DFS(r)

# u 정보 입력 및 정답 출력
for _ in range(q):
    u = int(input())
    print(dp[u])
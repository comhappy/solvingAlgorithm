# 사회망 서비스(SNS)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(n):  # n을 루트로 하는 트리의 얼리어답터를 구하는 함수
    visited[n] = 1  # 방문처리

    dp[n][1] = 1

    # 자식들을 순회
    for i in graph[n]:
        if visited[i] == 0:
            DFS(i)

            dp[n][0] += dp[i][1] # 부모가 얼리어답터가 아닌 경우, 자식이 얼리어답터여야함.
            dp[n][1] += min(dp[i][0], dp[i][1])  # 부모가 얼리어답터인 경우, 자식은 둘 중에 하나여야함.
        

n = int(input())

graph = [[] for _ in range(n + 1)]  # 관계를 나타내는 graph

for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# DP, DFS를 활용한 풀이방법
dp = [[0, 0] for _ in range(n + 1)] # dp[i][0]는 i번째 노드가 얼리어답터가 아닌 경우 얼리어답터의 개수
visited = [0 for _ in range(n + 1)]

DFS(1)

print(min(dp[1]))
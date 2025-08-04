import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 그래프에서 DFS
def dfs(s, depth):
    global result

    if depth == 5 or result == True:
        result = True
        return

    visited[s] = True

    # 하위 노드에 대해 dfs
    for i in range(len(A[s])):
        if visited[A[s][i]] != True:
            dfs(A[s][i], depth + 1)

    visited[s] = False

N, M = map(int, input().split())

# 인접리스트 구현(2차원 배열)
A = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    s, e = map(int, input().split())

    A[s].append(e)
    A[e].append(s)

# 모든 노드에 대해 dfs
result = False  # 가지치기 역할을 해주는 장치

for i in range(len(A)):
    dfs(i, 1)

    if result == True:
        break

if result:
    print(1)
else:
    print(0)
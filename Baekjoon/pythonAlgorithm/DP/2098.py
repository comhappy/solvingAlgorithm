# 외판원 순회(TSP)

def DP(s):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    visited = [0 for _ in range(n)]

    answer = 0

    for _ in range(n):
        dis = max(A[s])

        for i in range(n):
            if A[s][i] != 0 and visited[i] == 0 and A[s][i] < dis:
                e = i

        visited[e] = 1  # 방문처리
        answer += A[s][e]   # 거리 증가

        s = e

    return answer



n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))

answer = 0

for i in range(n):
    dist = DP(i)

    if answer == 0:
        answer = dist
    elif dist < answer:
        answer = dist

print(answer)
# DFS를 사용하는 문제, DFS의 횟수를 구하는 문제

import sys
sys.setrecursionlimit(10000)

def DFS(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:    # 좌표밖으로 벗어난 경우
        return False
    elif graph[y][x] == 0:    # 방문한 경우
        return False
    else:
        graph[y][x] = 0     # 방문표시
        
        DFS(x, y - 1)   # DFS 실행
        DFS(x, y + 1)
        DFS(x - 1, y)
        DFS(x + 1, y)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]   # 2차원으로 graph 만들기

    # 배추위치 표시
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 정답 구하기
    answer = 0

    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                DFS(i, j)
                answer += 1

    print(answer)
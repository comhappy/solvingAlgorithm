# N-Queen 문제, BackTracking 유형의 유명한 문제
# 모든 체스판을 DFS 해야하나?

def add_queen(i, j, graph):
    graph_copy = [[0 for _ in range(N)] for _ in range(N)]

    for a in range(N):
        for b in range(N):
            graph_copy[a][b] = graph[a][b]

    # x축, y축
    for xy in range(N):
        graph_copy[xy][j] = 1
        graph_copy[i][xy] = 1

    # 대각선
    x, y = i, j
    while(x >= 0 and x < N and y >=0 and y < N):    # 둘다 감소, 왼쪽 위 방향
        graph_copy[x][y] = 1
        x -= 1
        y -= 1

    x, y = i, j
    while(x >= 0 and x < N and y >=0 and y < N):    # 둘다 증가, 오른쪽 아래 방향
        graph_copy[x][y] = 1
        x += 1
        y += 1        

    x, y = i, j
    while(x >= 0 and x < N and y >=0 and y < N):    # x 증가, y 감소, 오른쪽 위 방향
        graph_copy[x][y] = 1
        x += 1
        y -= 1
        
    x, y = i, j
    while(x >= 0 and x < N and y >=0 and y < N):    # x 감소, y 증가, 왼쪽 아래 방향
        graph_copy[x][y] = 1
        x -= 1
        y += 1

    return graph_copy        


def DFS(x, y, queen, graph):
    global result

    if queen == N:  # queen의 개수가 N개
        result += 1

        return True
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0:    # queen을 둘 수 있는 경우
                    queen += 1      # queen을 배치

                    # graph 상태 복사
                    graph_copy = add_queen(i, j, graph) # queen의 좌표값 변경

                    DFS(i, j, queen, graph_copy)

                    queen -= 1

                    # # 복사한 graph 원상복구
                    # for a in range(N):
                    #     for b in range(N):
                    #         graph[a][b] = graph_copy[a][b]



N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

result = 0
queen = 0
DFS(0, 0, queen, graph)

print(result)
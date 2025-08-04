# 연구소

import sys, copy
sys.stdin.readline

def Virus(si, sj, virus_graph):
    if si >= 0 and sj >= 0 and si < N and sj < M and virus_graph[si][sj] == 0:    # 좌표를 만족하는 경우, 빈 공간인 경우
        virus_graph[si][sj] = 2
        
        # 4방향 확산
        Virus(si, sj - 1, virus_graph)
        Virus(si, sj + 1, virus_graph)
        Virus(si - 1, sj, virus_graph)
        Virus(si + 1, sj, virus_graph)
   
    return
                

def DFS(depth, index):  # 모든 벽의 경우를 찾아야하나?, depth는 벽의 개수를 의미2
    global result
    
    if depth == 3:
        # 바이러스 확산
        virus_graph = copy.deepcopy(graph)

        # 함수를 통한 바이러스 확산
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2:
                    Virus(i, j - 1, virus_graph)
                    Virus(i, j + 1, virus_graph)
                    Virus(i - 1, j, virus_graph)
                    Virus(i + 1, j, virus_graph)

        # 반복문을 통한 바이러스 확산
        flag = True

        while(flag):
            change = False

            for i in range(N):
                for j in range(M):
                    if virus_graph[i][j] == 0:
                        if  (j - 1) >= 0:  # 바이러스 확산 가능성이 있는 칸
                            if virus_graph[i][j - 1] == 2:
                                virus_graph[i][j] = 2

                                change = True

                        if (j + 1) < M:
                            if virus_graph[i][j + 1] == 2:
                                virus_graph[i][j] = 2

                                change = True

                        if (i - 1) >= 0:
                            if virus_graph[i - 1][j] == 2:
                                virus_graph[i][j] = 2

                                change = True

                        if (i + 1) < N:
                            if virus_graph[i + 1][j] == 2:
                                virus_graph[i][j] = 2

                                change = True
            
            if change:
                flag = True
            else:
                flag = False


        # 안전영역 계산
        safe_area = 0

        for i in range(N):
            for j in range(M):
                if virus_graph[i][j] == 0:
                    safe_area += 1

        if safe_area > result:
            result = safe_area

    else:   # 벽세우기
        for idx in range(index, N * M):
            i = idx // M
            j = idx % M

            if graph[i][j] == 0:    # 벽을 세울 수 있는 경우
                graph[i][j] = 1
                DFS(depth + 1, idx)
                graph[i][j] = 0

    

N, M = map(int, input().split())
graph = list()

for _ in range(N):
    graph.append(list(map(int, input().split())))

result = 0
DFS(0, 0)    #  depth와 순서

print(result)

# 경사로

def check(a, b, c):
    visited = [0 for _ in range(n)] # 경사로 처리를 위한 방문 배열

    if c == 1:  # 행 검사, a는 고정
        for i in range(1, n):
            if graph[a][i - 1] - graph[a][i] > 1 or graph[a][i - 1] - graph[a][i] < -1:
                return 0
            elif graph[a][i - 1] - graph[a][i] == -1:    # 경사로를 이용해 올라가는 경우
                # 경사로 검사(i-l ~ i-1)
                if i - l < 0:
                    return 0
                
                block = graph[a][i - l]
                for k in range(i - l, i):
                    if 0 <= k < n:
                        if block != graph[a][k] or visited[k] == 1: # 높이차이가 나거나 경사로가 존재하는 경우
                            return 0
                        else:
                            visited[k] = 1
                    else:
                        return 0

            elif graph[a][i - 1] - graph[a][i] == 1:   # 경사로를 이용해 내려가는 경우
                # 경사로 검사(i ~ i+l)
                block = graph[a][i]
                for k in range(i, i + l):
                    if 0 <= k < n:
                        if block != graph[a][k] or visited[k] == 1: # 높이차이가 나거나 경사로가 존재하는 경우
                            return 0
                        else:
                            visited[k] = 1
                    else:
                        return 0
        return 1

    if c == 2:  # 열 검사, b는 고정
        for i in range(1, n):
            if graph[i - 1][b] - graph[i][b] > 1 or graph[i - 1][b] - graph[i][b] < -1:
                return 0
            elif graph[i - 1][b] - graph[i][b] == -1:    # 경사로를 이용해 올라가는 경우
                # 경사로 검사(i-l ~ i-1)
                if i - l < 0:
                    return 0
                
                block = graph[i - l][b]
                for k in range(i - l, i):
                    if 0 <= k < n:
                        if block != graph[k][b] or visited[k] == 1: # 높이차이가 나거나 경사로가 존재하는 경우
                            return 0
                        else:
                            visited[k] = 1
                    else:
                        return 0

            elif graph[i - 1][b] - graph[i][b] == 1:   # 경사로를 이용해 내려가는 경우
                # 경사로 검사(i ~ i+l)
                block = graph[i][b]
                for k in range(i, i + l):
                    if 0 <= k < n:
                        if block != graph[k][b] or visited[k] == 1: # 높이차이가 나거나 경사로가 존재하는 경우
                            return 0
                        else:
                            visited[k] = 1
                    else:
                        return 0
        return 1


n, l = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
answer = 0

# 행 검사
for i in range(n):
    answer += check(i, 0, 1)

# 열 검사
for i in range(n):
    answer += check(0, i, 2)

print(answer)
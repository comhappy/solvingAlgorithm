# 점프

def DFS(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    
    if visited[x][y] == -1:     # 방문하지 않은 경우
        visited[x][y] = 0
    
        for dx, dy in [[jump[x][y], 0], [0, jump[x][y]]]:   # 탐색방향(오른쪽, 아래쪽)
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                visited[x][y] += DFS(nx, ny)    # 각각에 방향에서 가능한 수를 더해줌

    return visited[x][y]
    

n = int(input())
jump = list(list(map(int, input().split())) for _ in range(n))
visited = [[-1 for _ in range(n)] for _ in range(n)]    # 각 좌표에서 도달 가능한 경우의 수

DFS(0, 0)

print(visited[0][0])
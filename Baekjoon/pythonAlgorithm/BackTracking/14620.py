# 꽃길

def check_flower(x, y):
    if 1 <= x < n - 1 and 1 <= y < n - 1:    # 씨앗을 심을 수 있는 위치
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if visited[nx][ny] == 1:    # 꽃이 겹치는 경우
                return False
            
        return True
    else:
        return False
    
def flower(x, y, z):    # z == 0, 꽃 지우기, z == 1, 꽃 심기
    var_cost = 0
    
    visited[x][y] = z
    var_cost += cost[x][y]

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x + dx, y + dy

        visited[nx][ny] = z
        var_cost += cost[nx][ny]

    return var_cost


def DFS(index, count_flower):
    global count_cost, answer

    if count_flower == 3:
        answer = min(answer, count_cost)
        return

    for i in range(index, n*n):
        x = i // n
        y = i % n
        
        if visited[x][y] == 0 and check_flower(x, y):  # 꽃을 심을 수 있는 경우
            count_cost += flower(x, y, 1) # 꽃 심기, 계산
            DFS(i + 1, count_flower + 1)
            count_cost -= flower(x, y, 0) # 꽃 지우기, 계산


n = int(input())
cost = list(list(map(int, input().split())) for _ in range(n))

# 좌표 중 3개의 점을 선택, 비용을 계산해서 최소값을 구함
visited = [[0 for _ in range(n)] for _ in range(n)]
count_cost = 0
answer = 20000
DFS(0, 0)
print(answer)
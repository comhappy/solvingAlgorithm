# NM과 K

def DFS(index, number, depth):
    global answer

    if depth == k:  # 선택 완료
        answer = max(answer, number)
        return
    elif index == n * m:    # 끝까지 탐색한 경우
        return
    else:
        x, y = index // m, index % m
        
        flag = 0

        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 1:    # index에 접근 불가
                    flag = 1
                    break

        if flag == 0:
            visited[x][y] = 1
            DFS(index + 1, number + A[x][y], depth + 1)
            visited[x][y] = 0
            
        DFS(index + 1, number, depth)


def DFS2(index, number, depth):
    global answer

    if depth == k:
        answer = max(answer, number)
        return
    elif index == n * m:
        return
    else:
        for i in range(index, n * m):
            x, y = i // m, i % m
            flag = 1

            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 1:    # index에 접근 불가
                        flag = 0
                        break

            if flag:
                visited[x][y] = 1
                DFS2(i + 1, number + A[x][y], depth + 1)
                visited[x][y] = 0
            

n, m, k = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(n))

visited = [[0 for _ in range(m)] for _ in range(n)]
answer = -10000 * n * m

DFS2(0, 0, 0)

print(answer)
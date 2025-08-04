# 감시 피하기

def DFS(point, depth):
    global answer

    # 정답이 구해진 경우
    if answer == "YES":
        return
    # 검사
    elif depth == 3:    # 선생님 위치를 고려한 학생 찾기
        for tx, ty in teacher:
            for i in range(tx, -1, -1):  # 위
                if graph[i][ty] == "O":
                    break
                if graph[i][ty] =="S":
                    return

            for i in range(tx, n):  # 아래
                if graph[i][ty] == "O":
                    break
                if graph[i][ty] =="S":
                    return

            for i in range(ty, n):  # 오른쪽
                if graph[tx][i] =="O":
                    break
                if graph[tx][i] =="S":
                    return

            for i in range(ty, -1, -1):  # 왼쪽
                if graph[tx][i] =="O":
                    break
                if graph[tx][i] =="S":
                    return
            
        answer = "YES"

        return
    else:
        for i in range(point, n * n):
            x = i // n
            y = i % n
            
            if graph[x][y] == "X":  # 빈공간인 경우
                graph[x][y] = "O"
                DFS(point + 1, depth + 1)
                graph[x][y] = "X"


n = int(input())

teacher = list()
graph = list(list(input().split()) for _ in range(n))

# 선생님 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == "T":
            teacher.append([i, j])

answer = "NO"
DFS(0, 0)

print(answer)
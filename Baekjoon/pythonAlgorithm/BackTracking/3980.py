# 선발 명단

def DFS(player):
    global answer, score

    if player == 11:
        answer = max(answer, sum(score))
    else:
        for i in range(11):
            if s[player][i] == 0:
                continue
            elif visited[i] == 0:
                score[player] = s[player][i]
                visited[i] = 1
                DFS(player + 1)
                visited[i] = 0       


c = int(input())

for _ in range(c):
    s = list(list(map(int, input().split())) for _ in range(11))

    answer = 0
    score = [0 for _ in range(11)]
    visited = [0 for _ in range(11)]

    DFS(0)

    print(answer)
# 미친 로봇

def permutation(x, y, value, depth):
    global answer

    if depth == n: # 단순한 경로인 경우
        answer += value
        return
    else:
        for i in range(4):  # 동서남북 움직임
            if p[i] != 0:
                nx, ny = x + EWSN[i][0], y + EWSN[i][1]

                if 0 <= nx < 2*n + 1 and 0 <= ny < 2*n + 1:   # 좌표를 만족하고, 단순한 경로인 경우
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        permutation(nx, ny, value * p[i] / 100, depth + 1)
                        visited[nx][ny] = 0


info = list(map(int, input().split()))
n = info[0]
p = info[1:]

visited = [[0 for _ in range(2*n + 1)] for _ in range(2*n + 1)]
visited[n][n] = 1   # 처음 위치
EWSN = [[0, 1], [0, -1], [1, 0], [-1, 0]]

answer = 0
permutation(n, n, 1, 0)
print(answer)

# 모든 경로 > 순열로 구할 수 있음.(중복허용)
# 로봇의 경로가 단순할 확률 = 단순할 확률 / 전체 경로 확률
# 단순함을 어떻게 판단? > 경로를 의미하는 2차원 배열로 판단
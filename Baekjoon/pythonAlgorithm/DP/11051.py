# 이항 계수 2

n, k = map(int, input().split())

C = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

print(C[n][k] % 10007)
# 합분해

n, k = map(int, input().split())
answer = [[0 for _ in range(n + 1)] for _ in range(k + 1)]  # k개로 n을 만드는 경우의 수

# 0을 만드는 경우는 1가지
for i in range(1, k + 1):
    answer[i][0] = 1

# 나머지 DP 테이블 채우기
for i in range(1, k + 1):
    for j in range(1, n + 1):
        answer[i][j] = answer[i - 1][j] + answer[i][j - 1]
        answer[i][j] %= 1000000000

print(answer[k][n])
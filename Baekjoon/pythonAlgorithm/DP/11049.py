# 행렬 곱셈 순서

def DP():   # s ~ e까지 곱셈의 최소를 구하는 DP 함수
    dp = [[0 for _ in range(n)] for _ in range(n)]  # dp[s][e] : s ~ e 까지 행렬의 최소 곱셈횟수

    # 나머지 DP 테이블 채우기
    for i in range(n - 1, -1, -1):  # 역순으로 채워야 함
        for j in range(i + 1, n):
            for k in range(i, j):
                num = dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]  # 정답이 될 수 있는 값

                if dp[i][j] == 0:
                    dp[i][j] = num
                elif dp[i][j] > num:
                    dp[i][j] = num

    return dp[0][n - 1]

n = int(input())
matrix = list(list(map(int, input().split())) for _ in range(n))    # 행렬의 크기

answer = DP()
print(answer)
# 파일 합치기
# 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나간다.
# 연속이 되는 것이 핵심

import sys
input = sys.stdin.readline

def DP():
    dp = [[0 for _ in range(k)] for _ in range(k)]  # dp[s][e] : s ~ e까지 파일의 최소 크기

    # 초기값 세팅(누적합으로 설정)
    for i in range(k):
        dp[i][i] = file[i]

        for j in range(i + 1, k):
            dp[i][j] = dp[i][j - 1] + file[j]

    # DP 테이블 갱신 
    for i in range(k):
        dp[i][i] = 0

    for i in range(2, k):
        for j in range(k - i):
            s = j
            e = j + i

            size = dp[s][s] + dp[s + 1][e]

            # 최소값 찾기
            for n in range(s, e):
                if size > dp[s][n] + dp[n + 1][e]:
                    size = dp[s][n] + dp[n + 1][e]

            dp[s][e] += size

    print(dp[0][k - 1])


t = int(input())

for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))

    DP()
# 1학년

import sys
input = sys.stdin.readline


n = int(input())
num = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n - 1)]    # dp[i][j]는 num[i]까지 사용했을때 j를 만드는 경우의 수

dp[0][num[0]] = 1   # 기저상태 저장, 첫번째 숫자로 만들 수 있는 수

for i in range(1, n - 1):
    for j in range(0, 21):
        # ex) j = 2, num[i] = 2 인 경우
        # 이전의 수의 계산 결과가 0, 4 인 경우 각각 +2, -2를 하면 된다.
        if 0 <= j + num[i] <= 20:
            dp[i][j] += dp[i - 1][j + num[i]]   
        if 0 <= j - num[i] <= 20:
            dp[i][j] += dp[i - 1][j - num[i]]

print(dp[n - 2][num[n - 1]])
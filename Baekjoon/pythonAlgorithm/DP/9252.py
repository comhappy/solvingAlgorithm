# LCS 2

A = input()
B = input()

# dp[i][j]의 의미 : 문자열 A에서 i번째까지 문자열 B에서 j번째까지 비교했을 때, 가능한 LCS
dp = [["" for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:    # 추가되는 문자가 같은 경우
            dp[i][j] = dp[i - 1][j - 1] + A[j - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

if len(dp[len(B)][len(A)]):
    print(len(dp[len(B)][len(A)]))
    print(dp[len(B)][len(A)])
else:
    print(0)
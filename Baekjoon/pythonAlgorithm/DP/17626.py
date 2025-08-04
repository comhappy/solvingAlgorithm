# Four Squares

import math

n = int(input())
dp = [4 for _ in range(n + 1)]  # n을 만들때 필요한 최소 개수

# 제곱수 만들어주기
for i in range(int(n ** (1/ 2)) + 1):
    dp[i ** 2] = 1

# 나머지 부분 채우기
for i in range(n + 1):
    if dp[i] != 1:
        for j in range(int(i ** (1/ 2)), 0, -1):
            count = dp[i - j ** 2] + 1

            if count == 2:
                dp[i] = 2
                break

            elif count < dp[i]:
                dp[i] = count

print(dp[n])
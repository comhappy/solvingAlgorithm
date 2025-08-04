# 돌 게임 2

n = int(input())

if n == 1:
    print("CY")
elif n == 2:
    print("SK")
elif n == 3:
    print("CY")
else:
    dp = [n for _ in range(n + 1)]  # 돌을 가져가는 횟수

    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    
    for i in range(4, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 1]) + 1

    if dp[n] % 2 == 0:
        print("SK")
    else:
        print("CY")

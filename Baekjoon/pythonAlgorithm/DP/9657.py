# 돌 게임 3

n = int(input())

if n == 1:
    print("SK")
elif n == 2:
    print("CY")
elif n == 3:
    print("SK")
elif n == 4:
    print("SK")
else:
    dp = [0 for _ in range(n + 1)]

    dp[1], dp[2], dp[3], dp[4] = 1, 2, 1, 1

    for i in range(5, n + 1):
        if dp[i - 1] == dp[i - 3] and dp[i - 3] == dp[i - 4]:
            dp[i] = dp[i - 1] + 1
        else:   # 상근이가 무조건 이기는 경우
            dp[i] = 1
    
    if dp[n] % 2 == 0:
        print("CY")
    else:
        print("SK")
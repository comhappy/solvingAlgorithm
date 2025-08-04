# 앱
# 합이 m 이상이되는 최저의 cost를 찾는 문제.

def DP():
    dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]  # 가로는 cost, 세로는 메모리 사용 개수를 나타냄

    for i in range(1, n + 1):
        for j in range(sum(cost) + 1):
            if j >= cost[i - 1]:    # 해당 memory를 사용할 수 있는 경우
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    for i in range(sum(cost) + 1):
        for j in range(n + 1):
            if dp[j][i] >= m:
                print(i)

                return


n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

DP()
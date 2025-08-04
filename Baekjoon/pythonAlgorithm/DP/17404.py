# RGB거리 2

def DP(color):
    dp = [[1000 * 1000 + 1 for _ in range(3)] for _ in range(n + 1)]

    dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0

    if color == "R":
        dp[1][0] = RGB[0][0]
        dp[2][0], dp[2][1], dp[2][2] = 1000 * 1000 + 1, RGB[1][1] + RGB[0][0], RGB[1][2] + RGB[0][0]
    elif color == "G":
        dp[1][1] = RGB[0][1]
        dp[2][0], dp[2][1], dp[2][2] = RGB[1][0] + RGB[0][1], 1000 * 1000 + 1, RGB[1][2] + RGB[0][1]
    elif color == "B":
        dp[1][2] = RGB[0][2]
        dp[2][0], dp[2][1], dp[2][2] = RGB[1][0] + RGB[0][2], RGB[1][1] + RGB[0][2], 1000 * 1000 + 1

    for i in range(3, n + 1):
        dp[i][0] = RGB[i - 1][0] + min(RGB[i - 2][1] + min(dp[i - 2][0], dp[i - 2][2]), RGB[i - 2][2] + min(dp[i - 2][0], dp[i - 2][1]))
        dp[i][1] = RGB[i - 1][1] + min(RGB[i - 2][0] + min(dp[i - 2][1], dp[i - 2][2]), RGB[i - 2][2] + min(dp[i - 2][1], dp[i - 2][0]))
        dp[i][2] = RGB[i - 1][2] + min(RGB[i - 2][0] + min(dp[i - 2][1], dp[i - 2][2]), RGB[i - 2][1] + min(dp[i - 2][0], dp[i - 2][2]))

    if color == "R":
        return min(dp[n][1], dp[n][2])
    elif color == "G":
        return min(dp[n][0], dp[n][2])
    elif color == "B":
        return min(dp[n][0], dp[n][1])


n = int(input())
RGB = list(list(map(int, input().split())) for _ in range(n))

print(min(DP("R"), DP("G"), DP("B")))
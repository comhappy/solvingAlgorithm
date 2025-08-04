# 지름길

n, d = map(int, input().split())

road = list()

for _ in range(n):
    s, e, r = map(int, input().split())

    road.append([e, s, r])

road.sort()

dp = [i for i in range(d + 1)]

for e, s, r in road:
    if e <= d:  # 도착지점을 넘지 않는 경우
        dp[e] = min(dp[e], dp[s] + r)

        for i in range(e + 1, d + 1):
            dp[i] = min(dp[i], dp[e] + (i - e))

print(dp[d])
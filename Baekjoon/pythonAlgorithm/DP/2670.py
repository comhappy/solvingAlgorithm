# 연속부분최대곱

n = int(input())
f_num = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    f_num[i] = float(input())

dp[0] = f_num[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] * f_num[i], f_num[i])

print("%0.3f" % max(dp))
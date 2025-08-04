# 수열

n = int(input())
A = list(map(int, input().split()))

dp_up = [1 for _ in range(n)]
dp_down = [1 for _ in range(n)]

for i in range(1, n):
    if A[i - 1] <= A[i]:
        dp_up[i] = dp_up[i - 1] + 1

    if A[i - 1] >= A[i]:
        dp_down[i] = dp_down[i - 1] + 1

print(max(max(dp_up), max(dp_down)))
# 피보나치 수

n = int(input())

answer = [0 for _ in range(n + 1)]

answer[1] = 1

for i in range(2, n + 1):
    answer[i] = answer[i - 2] + answer[i - 1]

print(answer[n])
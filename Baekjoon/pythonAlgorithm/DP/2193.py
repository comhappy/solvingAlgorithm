# 이친수

n = int(input())

answer = [1 for _ in range(n + 1)]

if n <= 2:
    print(answer[n])
else:
    for i in range(3, n + 1):
        answer[i] = answer[i - 2] + answer[i - 1]
    print(answer[n])
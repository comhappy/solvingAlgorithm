# 피보나치 수 2

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    answer = [0 for _ in range(n + 1)]

    answer[1] = 1
    answer[2] = 1

    for i in range(3, n + 1):
        answer[i] = answer[i - 1] + answer[i - 2]

    print(answer[n])
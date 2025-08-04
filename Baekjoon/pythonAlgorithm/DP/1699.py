# 제곱수의 합

n = int(input())
answer = [i for i in range(n + 1)]

for i in range(n + 1):
    if i ** 2 <= n:
        answer[i ** 2] = 1
    else:
        break

for i in range(n + 1):
    j = 1
    while(1):
        if answer[i] > answer[j * j] + answer[i - j * j]:
            answer[i] = answer[j * j] + answer[i - j * j]

        j += 1

        if j * j > i:
            break

print(answer[n])
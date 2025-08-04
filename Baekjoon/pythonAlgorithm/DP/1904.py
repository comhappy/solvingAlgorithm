# 01 타일

n = int(input())

if n == 1:
    print(1)    # 1
elif n == 2:
    print(2)    # 00, 11
else:
    answer = [0 for _ in range(n + 1)]

    answer[1] = 1
    answer[2] = 2

    for i in range(3, n + 1):
        answer[i] = (answer[i - 1] + answer[i - 2]) % 15746   # 뒤에 1, 00을 붙이는 경우

    print(answer[n])
# 타일 채우기

n = int(input())

if n == 1:
    print(0)
else:
    answer = [0 for _ in range(n + 1)]
    answer[0] = 1
    answer[2] = 3

    for i in range(4, n + 1, 2):
        answer[i] = answer[i - 2] * answer[2]

        for j in range(i - 4, -1, -2):
            answer[i] += answer[j] * 2
            
    print(answer[n])
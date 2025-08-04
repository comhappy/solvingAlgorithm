# 정수 삼각형

import sys
input = sys.stdin.readline

def DP():
    answer[0][0] = num[0][0]

    for i in range(1, n):
        for j in range(0, len(num[i])):
            if j == 0:
                answer[i][j] = answer[i - 1][j] + num[i][j]
            elif j == (len(num[i]) - 1):
                answer[i][j] = answer[i - 1][j - 1] + num[i][j]
            else:
                answer[i][j] = max(answer[i - 1][j - 1], answer[i - 1][j]) + num[i][j]

    print(max(answer[n - 1]))


n = int(input())
num = list()
answer = list()

for i in range(n):
    num.append(list(map(int, input().split())))
    answer.append([0 for _ in range(len(num[i]))])

DP()
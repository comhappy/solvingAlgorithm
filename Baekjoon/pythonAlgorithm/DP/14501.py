# 퇴사

import sys
input = sys.stdin.readline

def DP():   # x일차에 선택 가능한 상담의 이익 = max(x - 1 일차 이익, 선택한 이익 + x - t일차의 이익)
    answer = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):   # n일차의 최대 이익을 구함
        max_p = answer[i - 1]
        for j in value[i]:  # n일차에 획득할 수 있는 이익
            ti, pi = j

            p = max(answer[i - 1], pi + answer[i - ti])

            if max_p < p:
                max_p = p

        answer[i] = max_p
    
    print(answer[n])


n = int(input())
value = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    t, p = map(int, input().split())

    if 1 <= i + t - 1 <= n:
        value[i + t - 1].append([t, p])

DP()
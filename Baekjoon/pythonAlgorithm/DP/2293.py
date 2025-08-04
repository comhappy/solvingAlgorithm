# 동전 1

import sys, copy
input = sys.stdin.readline

def DP():
    answer = [0 for _ in range(k + 1)]

    # 초기값 설정
    answer[0] = 1

    # DP 테이블 채우기
    for i in range(n):
        for j in range(1, k + 1):
            if j - coin[i] >= 0:
                answer[j] = answer[j] + answer[j - coin[i]]

    print(answer[k])


n, k = map(int, input().split())
coin = list()

for _ in range(n):
    coin.append(int(input()))

coin.sort()
DP()
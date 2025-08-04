# 계단 오르기
# x 계단의 값은 전의 상황을 알아야 함
# ooxo, xoxo, oxoo 총 3가지 상황이 있음.

import sys
input = sys.stdin.readline

def DP():
    answer[1] = score[1]
    answer[2] = score[1] + score[2]

    for i in range(3, stair + 1):
        # answer[i - 3] + score[i - 1] = oxoo 인 상황, answer[i - 2] = ooxo, xoxo 인 상황
        answer[i] = max(answer[i - 3] + score[i - 1], answer[i - 2]) + score[i]

    print(answer[stair])


stair = int(input())
score = [0 for _ in range(stair + 1)]
answer = [0 for _ in range(stair + 1)]

for i in range(stair):
    score[i + 1] = int(input())

if stair == 1:
    print(score[1])
else:
    DP()
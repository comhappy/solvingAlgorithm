# 스티커
# 위쪽 스티커를 선택하는 경우, 다음 3가지 경우중 최댓값을 구함
# OXO XXO XO
# XXX OXX OX

# 아래쪽 스티커를 선택하는 경우, 다음 3가지 경우중 최댓값을 구함
# OXX XXX OX
# XXO OXO XO

import sys
input = sys.stdin.readline

def DP():
    answer = [[0 for _ in range(n + 1)] for _ in range(2)]

    answer[0][1] = score[0][0]
    answer[1][1] = score[1][0]

    for i in range(2, n + 1):
        for j in range(2):
            if j == 0:  # 위쪽 스티커를 선택하는 경우
                sc = max(answer[j + 1][i - 1], answer[j][i - 2], answer[j + 1][i - 2])
                answer[j][i] = sc + score[j][i - 1]
            else:   # 아래쪽 스티커를 선택하는 경우
                sc = max(answer[j - 1][i - 1], answer[j - 1][i - 2], answer[j][i - 2])
                answer[j][i] = sc + score[j][i - 1]
        
    print(max(answer[0][n], answer[1][n]))


t = int(input())

for _ in range(t):
    n = int(input())
    score = list(list(map(int, input().split())) for _ in range(2))

    DP()
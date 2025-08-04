# 평범한 배낭

import sys
input = sys.stdin.readline

def DP(item):
    answer = [[0 for _ in range(k + 1)] for _ in range(n)]  # 가로축은 가방 무게, 세로 축은 item의 종류를 뜻함.

    # 배열의 첫번째 줄 채우기
    w, v = item[0]

    for i in range(k + 1):
        if i >= w:
            answer[0][i] = v

    # 배열의 나머지 부분 채우기
    for i in range(1, n):
        w, v = item[i]

        for j in range(k + 1):
            if j - w >= 0:  # 새로운 item이 배낭에 들어갈 수 있는 경우
                answer[i][j] = max(answer[i - 1][j], answer[i - 1][j - w] + v)  # 이전 item의 최댓값 vs 새로운 item을 추가한 최댓값
            else:
                answer[i][j] = answer[i - 1][j]

    print(answer[n - 1][k])

    

n, k = map(int, input().split())
item = list()

for _ in range(n):
    w, v = map(int, input().split())
    item.append([w, v])

DP(item)
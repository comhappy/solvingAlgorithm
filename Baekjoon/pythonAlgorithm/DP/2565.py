# 전깃줄

import sys
input = sys.stdin.readline

def DP():
    answer = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if line[j][1] < line[i][1]:
                answer[i] = max(answer[i], answer[j] + 1)

    print(n - max(answer))  # 전체 전깃줄 - 최대로 선택한 전깃줄

n = int(input())
line = list(list(map(int, input().split())) for _ in range(n))

line.sort() # A를 기준으로 오름차순 정렬

DP()
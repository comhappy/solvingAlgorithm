# 연속합

import sys
input = sys.stdin.readline

def DP():   # 마지막으로 i를 더할때 최대값
    answer = [num[i] for i in range(n)]

    for i in range(1, n):
        answer[i] = max(num[i], answer[i - 1] + num[i])

    print(max(answer)) 
    print(num)
    print(answer)
            

n = int(input())
num = list(map(int, input().split()))

DP()
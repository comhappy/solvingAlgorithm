# 포도주 시식

import sys
input = sys.stdin.readline

def DP():
    if n == 1:
        print(grape[1])
    elif n == 2:
        print(grape[1] + grape[2])
    elif n == 3:
        print(max(grape[1] + grape[2], grape[2] + grape[3], grape[3] + grape[1]))
    else:
        answer = [0 for _ in range(n + 1)]
        answer[1] = grape[1]
        answer[2] = grape[1] + grape[2]
        answer[3] = max(grape[1] + grape[2], grape[2] + grape[3], grape[3] + grape[1])

        for i in range(4, n + 1):
            num1 = answer[i - 5] + grape[i - 3] + grape[i - 2] + grape[i]  # XOOXO
            num2 = answer[i - 3] + grape[i - 1] + grape[i]  # XOO
            num3 = answer[i - 4] + grape[i - 2] + grape[i - 1]  # XOOX

            answer[i] = max(num1, num2, num3)
        
        print(answer)
        print(max(answer))

n = int(input())
grape = [0]

for _ in range(n):
    grape.append(int(input()))

DP()
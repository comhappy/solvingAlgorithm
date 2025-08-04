# 포도주 시식

import sys
input = sys.stdin.readline

def DP():
    if n == 1:
        print(grape[1])
    elif n == 2:
        print(grape[1] + grape[2])
    else:
        answer = [0 for _ in range(n + 1)]

        answer[1] = grape[1]
        answer[2] = grape[1] + grape[2]

        for i in range(3, n + 1):
            num1 = answer[i - 2] + grape[i] # OXO
            num2 = answer[i - 3] + grape[i - 1] + grape[i]  # XOO
            num3 = answer[i - 1]    # X
            
            answer[i] = max(num1, num2, num3)

        print(answer)
        print(answer[n])

n = int(input())
grape = [0]

for _ in range(n):
    grape.append(int(input()))

DP()
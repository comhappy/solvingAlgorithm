# AC

from collections import deque
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    p = list(input().strip())
    n = int(input())
    number = input().strip()

    if n == 0:
        number = list()
    else:
        number = [0] + list(map(int, number[1:len(number) - 1].split(",")))

    s, e = 1, len(number) - 1
    reverse = 0 # 뒤집힌 횟수
    ef = 0  # error flag

    for i in range(len(p)):
        if p[i] == "R":
            reverse += 1
        elif p[i] == "D":
            if s > e:  # 원소가 0개인 경우
                print("error")
                ef = 1
                break
            else:
                if reverse % 2 == 0:    # 짝수번 뒤집힌 경우
                    s += 1
                elif reverse % 2 == 1:  # 홀수번 뒤집힌 경우
                    e -= 1

    if ef == 0:
        if reverse % 2 == 0:    # 짝수번 뒤집힌 경우
            print("[", end='')
            print(*number[s:e + 1], sep=',', end='')
            print("]")
        elif reverse % 2 == 1:  # 홀수번 뒤집힌 경우
            print("[", end='')
            print(*number[e:s - 1:-1], sep=',', end='')
            print("]")
                    

# 왜 안됨..
#====================================================================================
    que = deque()

    for i in range(len(number)):
        que.append(number[i])
    
    ef = 1
    reverse = 0  # reverse 횟수

    for i in range(len(p)):
        if p[i] == "R":
            reverse += 1
        if p[i] == "D":
            if not que: # que가 비어있는 경우
                print("error")
                ef = -1
            elif ef == 1:
                if reverse % 2 == 0:
                    que.popleft()
                elif reverse % 2 == 1:
                    que.pop()

    if ef == 1:
        if reverse % 2 == 0:
            print("[", end="")
            print(*que, sep=',', end='')
            print("]")
        else:
            que.reverse()

            print("[", end="")
            print(*que, sep=',', end='')
            print("]")
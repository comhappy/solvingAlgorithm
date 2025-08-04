# 괄호의 값

from collections import deque

xy = input()

answer = 0  # 정답이 되는 점수
score = 1   # 중간계산을 위한 점수

stack = deque()
sp = -1  # stack pointer

stack.append(xy[0])
sp += 1

if xy[0] == "(":
    score = 2
elif xy[0] == "[":
    score = 3

for i in range(1, len(xy)):
    if xy[i] == "(":
        score *= 2

        stack.append(xy[i])
        sp += 1
    elif xy[i] == ")":
        if sp < 0 or stack[sp] != "(":
            answer = 0
            break
        else:
            if xy[i - 1] == "(":
                answer += score
                score /= 2

                stack.pop()
                sp -= 1
            else:
                score /= 2
                
                stack.pop()
                sp -= 1

    elif xy[i] == "[":
        score *= 3
        
        stack.append(xy[i])
        sp += 1
    elif xy[i] == "]":
        if sp < 0 or stack[sp] != "[":
            answer = 0
            break
        else:
            if xy[i - 1] == "[":
                answer += score
                score /= 3

                stack.pop()
                sp -= 1
            else:
                score /= 3

                stack.pop()
                sp -= 1

if sp == -1:
    print(int(answer))
else:
    print(0)
# 스택
# 스택의 사이즈는 무한인가? > 명령의 수가 최대 10,000개 이므로 사이즈는 10,000으로 설정

import sys
input = sys.stdin.readline      # 입력속도의 향상을 위해서 이렇게 작성해야함.

def push(s, x): # 정수 x를 스택에 넣음
    global s_pointer

    if s_pointer == 9999:
        return
    else:
        s_pointer += 1
        s[s_pointer] = x

def pop(s): # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력, 스택이 비어있을때는 -1을 출력
    global s_pointer
    
    if s_pointer == -1:
        print(-1)
    else:
        pop_num = s[s_pointer]
        s_pointer -= 1

        print(pop_num)

def size():    # 스택에 들어있는 정수의 개수를 출력
    if s_pointer == -1:
        print(0)
    else:
        print(s_pointer + 1)

def empty():   # 스택이 비어 있으면 1, 아니면 0을 출력
    if s_pointer == -1:
        print(1)
    else:
        print(0)

def top(s): # 스택의 가장 위에 있는 정수를 출력, 스택이 비어있을때는 -1을 출력
    if s_pointer == -1:
        print(-1)
    else:
        print(s[s_pointer])


N = int(input())

s = [0 for _ in range(N)]
s_pointer = -1

for _ in range(N):
    S = input().split()
    
    if S[0] == "push":
        push(s, S[1])
    elif S[0] == "pop":
        pop(s)
    elif S[0] == "size":
        size()
    elif S[0] == "empty":
        empty()
    elif S[0] == "top":
        top(s)

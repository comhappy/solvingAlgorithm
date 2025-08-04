# 1로 만들기, BFS를 사용해서 해결

from collections import deque

def BFS():
    if x == 1:  # 연산이 필요없는 경우
        print(0)
        return
    
    que = deque()
    depth = 1

    que.append(x)
    visited[x] = depth

    while(que):
        index = que.popleft()

        if index % 3 == 0:
            if visited[index // 3] == 0:
                que.append(index // 3)
                visited[index // 3] = visited[index] + 1

        if index % 2 == 0:
            if visited[index // 2] == 0:
                que.append(index // 2)
                visited[index // 2] = visited[index] + 1

        if visited[index - 1] == 0:
            que.append(index - 1)
            visited[index - 1] = visited[index] + 1

    print(visited[1] - 1)


x = int(input())
visited = [0 for _ in range(x + 1)]

BFS()
#---------------------------------------------------------------------------------------------
# 1로 만들기, DP를 사용해서 해결
# DP는 역순으로 생각하는 힘을 길러라, 1에서 만들 수 있는 수를 생각해볼 것

x = int(input())
number = [x for _ in range(x + 1)]  # DP를 위한 최댓값 설정

number[1] = 1

for i in range(1, x + 1):
    for index in [i * 3, i * 2, i + 1]:
        if 0 <= index <= x and number[index] > number[i] + 1:
            number[index] = number[i] + 1

print(number)
print(number[x] - 1)


#---------------------------------------------------------------------------------------------
# 1로 만들기, DP를 사용해서 해결

x = int(input())
number = [x for _ in range(x + 1)]  # DP를 위한 최댓값 설정
number[x] = 0

for i in range(x, 0, -1):   # 주어진 수부터 시작
    if i % 3 == 0 and 0 <= i // 3 <= x:  # 3으로 나누어지는 경우
        if number[i // 3] > number[i] + 1:
            number[i // 3] = number[i] + 1
    if i % 2 == 0 and 0 <= i // 2 <= x:  # 2로 나누어지는 경우
        if number[i // 2] > number[i] + 1:
            number[i // 2] = number[i] + 1
    if 0 <= i - 1 <= x:
        if number[i - 1] > number[i] + 1:
            number[i - 1] = number[i] + 1

print(number)
print(number[1])
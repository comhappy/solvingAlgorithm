# 뱀

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

# 사과의 위치
for _ in range(k):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 2

# 뱀의 방향 변환 횟수
l = int(input())
dir = ["R" for _ in range(21)]    # index 초 일때, 뱀의 머리 방향
dir_pre = 1

for _ in range(l):
    x, c = input().split()

    for i in range(dir_pre, int(x)):
        dir[i] = dir[dir_pre]

    dir_pre = int(x)

    

    dir[dir_pre] = c

print(dir)

snake = deque()
snake.append([0, 0])    # 뱀을 이루는 좌표

end = 1     # 종료 flag
time = 0
ordernum = 0

# while(end):
#     print(snake)

#     time += 1


#     # 개수에 다른 head, tail 처리
#     if len(snake) == 1:
#         head = snake.popleft()
#         hx, hy = head
#         tx, ty = head
#     else:
#         head = snake.popleft()
#         tail = snake.pop()
#         hx, hy = head
#         tx, ty = tail

#     print(hx, hy)

#     if dir == "R":  # 오른쪽으로 이동
#         if 0 <= hy + 1 < n and [hx, hy + 1] not in snake:
#             if graph[hx][hy + 1] == 2:    # 사과인 경우, tail을 잃지 않음
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx, hy + 1])
#                 snake.append([tx, ty])
#             else:
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx, hy + 1])
#         else:   # 이동 x
#             snake.appendleft([hx, hy])
#             end = 0

#     elif dir == "L":    # 왼쪽으로 이동
#         if 0 <= hy - 1 < n and [hx, hy - 1] not in snake:
#             if graph[hx][hy - 1] == 2:    # 사과인 경우, tail을 잃지 않음
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx, hy - 1])
#                 snake.append([tx, ty])
#             else:
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx, hy - 1])
#         else:   # 이동 x
#             snake.appendleft([hx, hy])
#             end = 0

#     elif dir == "U":    # 위로 이동
#         if 0 <= hx - 1 < n and [hx - 1, hy] not in snake:
#             if graph[hx - 1][hy] == 2:    # 사과인 경우, tail을 잃지 않음
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx - 1, hy])
#                 snake.append([tx, ty])
#             else:
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx - 1, hy])
#         else:   # 이동 x
#             snake.appendleft([hx, hy])
#             end = 0

#     elif dir == "D":    # 밑으로 이동
#         if 0 <= hx + 1 < n and [hx + 1, hy] not in snake:
#             if graph[hx + 1][hy] == 2:    # 사과인 경우, tail을 잃지 않음
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx + 1, hy])
#                 snake.append([tx, ty])
#             else:
#                 snake.appendleft([hx, hy])
#                 snake.appendleft([hx + 1, hy])
#         else:   # 이동 x
#             snake.appendleft([hx, hy])
#             end = 0

print(snake)
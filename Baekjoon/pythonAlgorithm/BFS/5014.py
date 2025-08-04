# 스타트링크

from collections import deque
import sys
input = sys.stdin.readline

def BFS(F, S, G, U, D):
    que = deque()
    visited = [False for _ in range(F)]
    count_button = 0
    
    if S == G:  # 이동하지 않아도 되는 경우
        return 0
    else:   # 이동해야하는 경우
        que.append([S, 1])
        visited[S - 1] = True
        
        while(que):
            floor, count_button = que.popleft()

            # 가능한 경우 계산
            up = floor + U
            down = floor - D

            if up == G  or down == G: # 목표에 도달한 경우
                return count_button
            
            # 목표에 도달하지 못한 경우
            if 1 <= up <= F:  # up 조건 확인
                if visited[up - 1] == False:
                    que.append([up, count_button + 1])
                    visited[up - 1] = True

            if 1 <= down <= F:  # down 조건 확인
                if visited[down - 1] == False:
                    que.append([down, count_button + 1])
                    visited[down - 1] = True

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(BFS(F, S, G, U, D))
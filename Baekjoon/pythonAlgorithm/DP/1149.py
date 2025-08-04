# RGB거리

import sys
input = sys.stdin.readline

def DP():
    cost = [[0 for _ in range(3)] for _ in range(n + 1)]    # index까지의 최소비용

    # 1번집의 cost
    cost[1][0] = color[1][0]
    cost[1][1] = color[1][1]
    cost[1][2] = color[1][2]

    # 2~n번집의 cost
    for i in range(2, n + 1):
        cost[i][0] = color[i][0] + min(cost[i - 1][1], cost[i - 1][2])
        cost[i][1] = color[i][1] + min(cost[i - 1][2], cost[i - 1][0])
        cost[i][2] = color[i][2] + min(cost[i - 1][0], cost[i - 1][1])
        
    print(min(cost[n]))


n = int(input())
color = [[0, 0, 0]]

for _ in range(n):
    color.append(list(map(int, input().split())))

DP()
# RGB거리

import sys
input = sys.stdin.readline

n = int(input())
before_cost = list(map(int, input().split()))
cost = [0, 0, 0]

for _ in range(n - 1):
    cost = list(map(int, input().split()))

    cost[0] = cost[0] + min(before_cost[1], before_cost[2])
    cost[1] = cost[1] + min(before_cost[0], before_cost[2])
    cost[2] = cost[2] + min(before_cost[0], before_cost[1])

    before_cost = cost

print(min(cost))
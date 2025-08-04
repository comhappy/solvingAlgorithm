# 작업

from collections import deque
import sys
input = sys.stdin.readline

def DP():   # 위상정렬을 이용한 DP
    dp = [0 for _ in range(n + 1)]
    que = deque()

    for i in range(1, n + 1):
        if edge[i] == 0:    # 선행 작업이 없는 경우
            que.append(i)
            dp[i] = time[i]

    while(que):
        task = que.popleft()

        for i in graph[task]:
            dp[i] = max(dp[i], dp[task] + time[i])
            edge[i] -= 1

            if edge[i] == 0:    # 선행작업이 없어진 경우
                que.append(i)

    print(max(dp))


n = int(input())
time = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
edge = [0 for _ in range(n + 1)]

for i in range(n):
    info = list(map(int, input().split()))

    time[i + 1] = info[0]
    edge[i + 1] = info[1]

    for j in range(2, info[1] + 2):
        graph[info[j]].append(i + 1)
        
DP()
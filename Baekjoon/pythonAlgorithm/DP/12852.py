# 1로 만들기 2

from collections import deque

def DP():
    dp = [[0, 0] for _ in range(n + 1)]  # 최소 연산횟수를 가지는 depth, index

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + 1 # depth
        dp[i][1] = i - 1 # index

        if i % 3 == 0:  # 3으로 나누어지는 경우
            if dp[i // 3][0] < dp[i][0]:
                dp[i][0] = dp[i // 3][0] + 1
                dp[i][1] = i // 3

        if i % 2 == 0:  # 2로 나누어지는 경우
            if dp[i // 2][0] < dp[i][0]:
                dp[i][0] = dp[i // 2][0] + 1
                dp[i][1] = i // 2


    print(dp[n][0]) # depth 출력
    
    # 순서 출력
    k = n
    print(k, end=' ')

    while(1):
        if k == 1:
            break

        print(dp[k][1], end=' ')
        k = dp[k][1]


def BFS():
    que = deque()
    que.append([n, []])
    visited = [0 for _ in range(n + 1)]

    while(que):
        index, numbers = que.popleft()
        numbers = numbers + [index]

        # 종료조건
        if index == 1:
            print(len(numbers) - 1)
            print(*numbers)

            return
        
        if index % 3 == 0 and visited[index // 3] == 0: # 3으로 나누어지고 방문하지 않은 경우
            visited[index // 3] = 1
            que.append([index // 3, numbers])
        if index % 2 == 0 and visited[index // 2] == 0: # 2로 나누어지고 방문하지 않은 경우
            visited[index // 2]  = 1
            que.append([index // 2, numbers])
        if index - 1 >= 0 and visited[index - 1] == 0: # 1을 더하는 경우
            visited[index - 1] = 1
            que.append([index - 1, numbers])
    

n = int(input())

#DP()
BFS()
# 숨바꼭질3
# 0-1 BFS

from collections import deque

def BFS(n, k):  # BFS를 사용하여 위치를 추척
    que = deque()
    visited = [100001 for _ in range(100001)]

    que.append(n)
    visited[n] = 0
    
    while(que):
        x = que.popleft()

        # 위치에 도달한경우
        if x == k:
            return visited[x]

        for i in [2 * x, x + 1, x - 1]:
            if 0 <= i <= 100000:    # 좌표를 만족
                if i == 2 * x and visited[x] < visited[i]:  # 갱신 기준을 판단
                    que.appendleft(i)
                    visited[i] = visited[x]
                elif visited[x] + 1 < visited[i]:   # 갱신 기준을 판단
                    que.append(i)
                    visited[i] = visited[x] + 1

n, k = map(int, input().split())

if n == k:
    print(0)
else:
    answer = BFS(n, k)
    print(answer)
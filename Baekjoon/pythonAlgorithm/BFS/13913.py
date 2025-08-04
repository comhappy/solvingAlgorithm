# 숨바꼭질 4

from collections import deque

n, k = map(int, input().split())
v = 100000

if n == k:
    print(0)
    print(n)
else:
    visited = [-1 for _ in range(v + 1)]

    que = deque()
    que.append(n)
    visited[n] = n

    while(que):
        point = que.popleft()

        if point == k:
            break

        for i in [point - 1, point + 1, point * 2]:
            if 0 <= i <= v and visited[i] == -1:
                que.append(i)
                visited[i] = point

    order = [k]
    index = k

    while(1):
        order.append(visited[index])
        index = visited[index]

        if index == n:
            break

    order.reverse()

    print(len(order) - 1)
    print(*order)
# 요세푸스 문제

from collections import deque

n, k = map(int, input().split())

que = deque()
for i in range(1, n + 1):
    que.append(i)

answer = list()

for _ in range(n):
    for i in range(k - 1):
        n = que.popleft()
        que.append(n)

    n = que.popleft()
    answer.append(n)

print("<", end='')
print(*answer, sep=", ", end='')
print(">")
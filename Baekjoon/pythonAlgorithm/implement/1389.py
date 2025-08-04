# 케빈 베이컨의 6단계 법칙

from collections import deque
import sys
input = sys.stdin.readline

def BFS(person):  # 케빈 베이컨 수를 찾아주는 함수
    que = deque()
    que.append(person)
    visited[person] = 1

    while(que):
        person = que.popleft()

        for i in graph[person]:     # BFS 탐색을 통한 방문처리
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[person] + 1

    return sum(visited)     # 정확한 표현은 sum(visited) - n


n, m = map(int, input().split())
graph = list(list() for _ in range(n))
visited = [0 for _ in range(n)]

# 연결 그래프 만들기
for _ in range(m):
    a, b = map(int, input().split())

    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

answer = 0
result = n ** 2

# BFS를 통한 케빈 베이컨 수를 찾고 최소값을 저장
for i in range(n):  
    num_of_kevin = BFS(i)
    visited = [0 for _ in range(n)]

    if num_of_kevin < result:
        result = num_of_kevin
        answer = i

print(answer + 1)
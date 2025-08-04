# 촌수계산
# 그래프를 만들고 BFS의 횟수를 구한다.

from collections import deque
import sys
input = sys.stdin.readline

def BFS(p): # 그래프를 탐색
    queue = deque()
    queue.append(graph[p])
    visited[p] = True

    depth = 1

    # depth를 구하는 것이 어려움.
    while(queue):   # 자식노드 탐색 부분, while문 실행 횟수 = depth
        c = queue.popleft()
        appendlist = list()

        for i in c:
            if i == b:  # 찾은 경우
                return depth
            elif visited[i] == False:
                for j in graph[i]:  # 자식노드를 취합해서 하나의 리스트로 추가
                    appendlist.append(j)
                visited[i] = True

        # 추가할 자식 노드가 있다면 추가, 존재하지 않는데 queue에 추가한다면, 무한루프 상태에 돌입함
        if appendlist:
            queue.append(appendlist)

        depth += 1

    return -1   # 관계가 없는 경우


n = int(input())
a, b = map(int, input().split())
m = int(input())

# 부모 자식 관계를 나타내는 무방향 그래프, 2차원 리스트로 표현
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

print(BFS(a))
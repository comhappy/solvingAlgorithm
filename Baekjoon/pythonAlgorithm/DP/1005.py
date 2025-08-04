# ACM Craft
# 위상정렬(진입 차수가 0인 노드를 큐에 넣어주고 큐가 빌때까지 탐색)

from collections import deque
import sys
input = sys.stdin.readline

def BFS(w):
    q = deque()
    q.append(w)
    depth = [0 for _ in range(n + 1)]   # depth 값이 같으면 동시에 건설 가능
    depth[w] = 1

    while(q):
        node = q.popleft()

        for i in graph[node]:
            q.append(i)
            depth[i] = depth[node] + 1

    answer = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        answer[depth[i]].append(d[i])

    result = 0
    for i in range(1, n + 1):
        if answer[i]:
            result += max(answer[i])

    print(answer)
    print(result)


def TPsort():
    q = deque()
    answer = [i for i in d]

    # 진입차수가 0인 노드를 큐에 추가, 시간 갱신
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            indegree[i] -= 1

    while(q):
        node = q.popleft()

        for i in graph[node]:
            indegree[i] -= 1
            answer[i] = max(answer[node] + d[i], answer[i])
            
            if indegree[i] == 0:    # 진입차수가 0인 경우
                q.append(i)
                
    print(answer[w])


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    d = [0]
    
    for i in list(map(int, input().split())):
        d.append(i)

    graph = [[] for _ in range(n + 1)]  # 위상정렬을 이용하는 graph
    indegree = [0 for _ in range(n + 1)]    # 진입차수를 나타내는 리스트
        
    for _ in range(k):
        s, e = map(int, input().split())

        graph[s].append(e)
        indegree[e] += 1

    w = int(input())

    TPsort()
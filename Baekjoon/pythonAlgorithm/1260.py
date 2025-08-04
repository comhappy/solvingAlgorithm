# 인접 리스트를 DFS, BFS 한 결과를 각각 출력하는 문제
# DFS, BFS를 구현할 수 있냐를 물어보는 것 같음

from collections import deque

def DFS(v): # 인접리스트의 index가 입력됨
    if visited[v] == False: # DFS로 노드에 접근
        print(v, end=" ")
        visited[v] = True
        
        for i in A[v]:
            DFS(i)
    else:
        return

def BFS(v):
    # BFS를 위한 dequeue 생성, 시작노드를 queue에 입력
    BFS_dequeue = deque()
    BFS_dequeue.append(v)
    visited[v] = True

    while(BFS_dequeue): # queue가 비어있을때까지 반복
        popV = BFS_dequeue.popleft()
        print(popV, end=" ")

        for i in A[popV]:
            if visited[i] == False:
                BFS_dequeue.append(i)
                visited[i] = True


N, M, V = map(int, input().split()) # 입력받은 값

# 인접 리스트 생성
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    s, e = map(int, input().split())

    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):  # 작은 번호부터 접근하기 위해 정렬
    A[i].sort()


DFS(V)
print()

# 도착정보 초기화
for i in range(N + 1):
    visited[i] = False

BFS(V)
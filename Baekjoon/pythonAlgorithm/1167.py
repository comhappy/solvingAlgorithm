# 트리의 지름 구하기
# 주어진 각 노드에서 BFS를 하면서, 노드 사이 거리를 최신화
# 모든 노드를 다 돌아서 최신화된 값을 확인 후, 최댓값이 트리의 지름이 된다.

from collections import deque

def BFS(v): # v 노드에서 각자 노드까지의 거리를 업데이트
    queue_BFS = deque()
    queue_BFS.append(v)
    visited_A[v] = True

    while queue_BFS:
        now_node = queue_BFS.popleft()

        for i in A[now_node]:
            next_node = i[0] - 1
            value = i[1]

            # 다음 노드가 방문한 노드가 아닌 노드에 대해
            if visited_A[next_node] == False:
                # 기존 거리값과 v ~ now_node ~ next_node 값을 비교 후 큰 값으로 갱신
                #if distance[next_node] < distance[now_node] + value:
                distance[next_node] = distance[now_node] + value

                # 다음 노드를 queue에 추가
                queue_BFS.append(next_node)
                visited_A[next_node] = True

    return max(distance)    # v ~ 각각의 노드까지의 최대거리를 return


V = int(input())

# 거리 정보를 저장할 1차원 배열, max 값만 추출하면 됨, (~ index까지의 거리)
distance = [0 for _ in range(V)]

# 노드 정보를 저장할 인접 리스트, i > j 일때 값 v, A[i][[i, v]]로 나타냄
A = [[] for _ in range(V)]
visited_A = [False for _ in range(V)]

for i in range(V):
    info = list(input().split())
    index = int(info[0]) - 1
    info = info[1:len(info) - 1]

    for j in range(0, len(info), 2):
        A[index].append([int(info[j]), int(info[j+1])])

# 임의의 한 점에서 BFS 후 최대 거리를 가지는 index에서 BFS 후 최대거리 구하기
maxdis = BFS(0)

maxindex = 0

for i in range(V):
    if distance[maxindex] < distance[i]:
        maxindex = i

distance = [0 for _ in range(V)]
visited_A = [False for _ in range(V)]

print(BFS(maxindex))
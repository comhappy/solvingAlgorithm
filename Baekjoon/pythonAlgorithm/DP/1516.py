# 게임 개발
# 위상정렬의 개념으로 문제 해결

from collections import deque

def TPsort():   # 위상정렬
    q = deque()
    answer = [i for i in time]

    for i in range(1, n + 1):   # 진입차수가 0인 노드를 큐에 추가
        if indegree[i] == 0:
            q.append(i)

    while(q):
        node = q.popleft()

        for i in graph[node]:
            indegree[i] -= 1    # 진입차수 감소

            answer[i] = max(answer[i], answer[node] + time[i])    # DP를 이용한 최소시간

            if indegree[i] == 0:
                q.append(i)

    # 정답출력 부분
    for i in answer[1:]:
        print(i)


n = int(input())

graph = [[] for _ in range(n + 1)]  # 방향그래프
indegree = [0 for _ in range(n + 1)]   # 진입차수를 나타냄
time = [0 for _ in range(n + 1)]

# 정보 입력 받기
for i in range(1, n + 1):
    info = list(map(int, input().split()))

    time[i] = info[0]

    # 방향그래프 생성
    for j in range(1, len(info) - 1):
        graph[info[j]].append(i)
        indegree[i] += 1

# 최소 시간 계산
TPsort()
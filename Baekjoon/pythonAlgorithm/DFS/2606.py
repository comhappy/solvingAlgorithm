# DFS를 사용하는 문제

def DFS(node):
    global result

    if visited[node] == True:   # 이미 방문한 경우
        return False
    else:
        visited[node] = True
        result += 1 # 방문한 노드 개수 추가
        
        for i in graph[node]:   # 연결되어 있는 노드를 방문
            DFS(i)


comnum = int(input())
edge = int(input())

# 무방향 그래프, 방문기록 생성
graph = [[] for _ in range(comnum + 1)]
visited = [False] * (comnum + 1)

for i in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

result = 0
DFS(1)
print(result - 1)   # 1번은 이미 걸렸으므로 빼주기
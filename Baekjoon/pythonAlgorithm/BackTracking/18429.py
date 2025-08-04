# 근손실

def DFS(weight, depth):
    global answer

    if weight < 500:
        return
    elif depth == n:
        answer += 1
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                weight += kit[i]
                
                DFS(weight - k, depth + 1)

                visited[i] = 0
                weight -= kit[i]
                

n, k = map(int, input().split())
kit = list(map(int, input().split()))

visited = [0 for _ in range(n)]
answer = 0
DFS(500, 0)
print(answer)
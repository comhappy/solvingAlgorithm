# 에너지 모으기

def DFS(k, energy, depth): # i번째 구슬 고르기
    global answer

    if depth == n - 2:  # 모든 구슬을 선택한 경우
        answer = max(answer, energy)

        return
    
    elif visited[k] == 1:   # 이미 방문한 경우
        return

    else:
        visited[k] = 1

        # 왼쪽에 있는 구슬
        for i in range(k - 1, -1, -1):
            if visited[i] == 0:
                a = w[i]

                break

        # 오른쪽에 있는 구슬
        for i in range(k + 1, n + 1):
            if visited[i] == 0:
                b = w[i]

                break

        for i in range(1, n - 1):
            DFS(i, energy + a * b, depth + 1)

        visited[k] = 0

        return
    

n = int(input())
w = list(map(int, input().split()))

# 구슬은 n - 2개 고를 수 있다.
answer = 0
visited = [0 for _ in range(n)]

for i in range(1, n - 1):
    DFS(i, 0, 0)

print(answer)
# 도영이가 만든 맛있는 음식

def DFS(depth, start):
    global taste_s, taste_b, answer

    if depth > 0:
        answer = min(answer, abs(taste_s - taste_b))
    
    for i in range(start, n):
        if visited[i] == 0:
            visited[i] = 1  # 재료를 사용
            taste_s *= food[i][0]
            taste_b += food[i][1]

            DFS(depth + 1, i)

            visited[i] = 0  # 재료를 사용
            taste_s /= food[i][0]
            taste_s = int(taste_s)
            taste_b -= food[i][1]


n = int(input())
food = list()

for _ in range(n):
    s, b = map(int, input().split())
    food.append([s, b])
    
answer = 1000000000
taste_s, taste_b = 1, 0
visited = [0 for _ in range(n)]

DFS(0, 0)

print(answer)
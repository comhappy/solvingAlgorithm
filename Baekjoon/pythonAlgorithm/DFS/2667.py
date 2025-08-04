#DFS 카테고리 문제


#DFS 실행
def DFS(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return
    elif Graph[x][y] == 0:   # 방문한 경우
        return
    else:   # 방문하지 않은 경우
        Graph[x][y] = 0
        global house
        house += 1

        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)

        # if x == 0:
        #     DFS(x+1, y)
        #     DFS(x, y+1)
        #     DFS(x, y-1)
        # elif y == 0:
        #     DFS(x+1, y)
        #     DFS(x-1, y)
        #     DFS(x, y+1)
        # elif x == N-1:
        #     DFS(x-1, y)
        #     DFS(x, y+1)
        #     DFS(x, y-1)
        # elif y == N-1:
        #     DFS(x+1, y)
        #     DFS(x-1, y)
        #     DFS(x, y-1)
        # else:
        #     DFS(x+1, y)
        #     DFS(x-1, y)
        #     DFS(x, y+1)
        #     DFS(x, y-1)

        


N = int(input())

# 단지 그래프 만들기
Graph = [] * N

for i in range(N):
    Graph.append((list(map(int, list(input())))))


# 정답 구하기
danji = 0
house_arr = []

for i in range(N):
    for j in range(N):
        if Graph[i][j] == 1:
            house = 0
            DFS(i, j)
            
            danji += 1
            house_arr.append(house)
            house = 0

print(danji)
house_arr.sort()

for i in house_arr:
    print(i)
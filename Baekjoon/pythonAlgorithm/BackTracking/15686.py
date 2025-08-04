# 치킨 배달
# 0은 빈 칸, 1은 집, 2는 치킨 집


def DFS(p): # p는 선택된 치킨집 좌표
    if len(shoplist) == M:     # 치킨집이 최대로 도달했을 때
        # 치킨거리 계산
        chicken_dis = 0     # 해당하는 치킨거리 저장

        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:    # 집인 경우
                    min_dis = list()    # 각각의 치킨집과 집의 치킨거리를 저장할 리스트

                    for [x, y] in shoplist:
                        min_dis.append(abs(x - i) + abs(y - j))

                    chicken_dis += min(min_dis)

        result.append(chicken_dis)

    else:
        for x in range(p, N**2):    # 치킨집을 찾음, 오름차순을 고려
            i = x // N
            j = x - N * i

            if graph[i][j] == 2:    # 치킨집인 경우
                shoplist.append([i, j])
                DFS(x + 1)
                shoplist.pop()
        
        return True


N ,M = map(int, input().split())

graph = list()

for i in range(N):
    graph.append(list(map(int, input().split())))

# 치킨집을 고른 후, 거리를 계산, 거리를 비교
# 2차원배열을 1차원으로 표현 graph[i][j] = (i * N + j), 치킨집 선택을 오름차순으로 하기 위해
shoplist = list()   # 추가된 치킨집 리스트
result = list()     # 각각의 치킨 거리를 저장할 리스트
DFS(0)
print(min(result))
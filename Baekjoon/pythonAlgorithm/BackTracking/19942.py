# 다이어트

import copy

def DFS(start, depth, current):
    global price, element, answer_element

    if current[0] >= mp and current[1] >= mf and current[2] >= ms and current[3] >= mv: # 최소 영양분 조건을 만족
        if price > current[4]:
            price = current[4]
            answer_element = copy.deepcopy(element)
        return
    else:
        for i in range(start, n):
            if visited[i] == 0:
                visited[i] = 1
                for j in range(5):
                    current[j] += info[i][j]
                element.append(i + 1)

                DFS(i, depth + 1, current)

                visited[i] = 0
                for j in range(5):
                    current[j] -= info[i][j]
                element.pop()


n = int(input())

mp, mf, ms, mv = map(int, input().split())  # 최소 영양성분 : 단백질, 지방, 탄수화물, 비타민
info = list(list(map(int, input().split())) for _ in range(n))  # 단백질, 지방, 탄수화물, 비타민, 가격

current = [0, 0, 0, 0, 0]   # 현재 단백질, 지방, 탄수화물, 비타민, 가격
visited = [0 for _ in range(n)]
price = 15 * 500
element = []
answer_element = []

DFS(0, 0, current)

if len(answer_element) != 0:
    print(price)
    print(*answer_element)
else:
    print(-1)
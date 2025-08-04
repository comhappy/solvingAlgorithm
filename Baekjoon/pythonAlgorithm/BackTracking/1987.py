# 알파벳
# 미로찾기 알고리즘을 생각해보자

def DFS(x, y):  # x, y에 방문함을 의미  
    global step, max_step

    if x < 0 or x >= R or y < 0 or y >= C:  # 좌표를 넘어가는 경우
        return False
    
    elif alphalist[ord(graph[x][y]) - 65] == True:  # 해당하는 알파벳을 방문한 경우
        # 최대 이동 개수 비교
        if step > max_step:
            max_step = step

        return False
    
    else:   # 성공적으로 방문한 경우
        alphalist[ord(graph[x][y]) - 65] = True
        step += 1

        DFS(x, y - 1)
        DFS(x, y + 1)
        DFS(x - 1, y)
        DFS(x + 1, y)

        alphalist[ord(graph[x][y]) - 65] = False
        step -= 1

        return True


R, C = map(int, input().split())
graph = list()

# graph 만들기
for _ in range(R):
    alpha = input()
    addlist = list()
    for i in alpha:
        addlist.append(i)
    graph.append(addlist)

# alphalist = list()  # 방문한 알파벳을 저장하는 리스트, 시간초과의 원인?

alphalist = [False for _ in range(26)]

step = 0
result = list()
max_step = 1

DFS(0, 0)

print(max_step)

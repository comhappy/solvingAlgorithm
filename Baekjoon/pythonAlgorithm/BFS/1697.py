# 숨바꼭질

from collections import deque

def BFS(n, k):
    if n == k:  # 이동할 필요가 없을때
        print(0)
        return
    
    que = deque()   # BFS에서 사용할 큐
    que.append(n)
    visitedN = [0 for _ in range(100001)]
    visitedN[n] = 1

    while(que):
        loc = que.popleft()

        loc1 = loc - 1    # 뒤로 한칸
        loc2 = loc + 1    # 앞으로 한칸
        loc3 = loc * 2    # 순간이동

        if loc1 == k or loc2 == k or loc3 == k: # 정답인 경우
            print(visitedN[loc])

            return

        if 0 <= loc1 <= 100000: # 범위 내에 있는 경우
            if visitedN[loc1] == 0: # 방문하지 않은 경우
                visitedN[loc1] = visitedN[loc] + 1
                que.append(loc1)
        
        if 0 <= loc2 <= 100000: # 범위 내에 있는 경우
            if visitedN[loc2] == 0: # 방문하지 않은 경우
                visitedN[loc2] = visitedN[loc] + 1
                que.append(loc2)

        if 0 <= loc3 <= 100000: # 범위 내에 있는 경우
            if visitedN[loc3] == 0: # 방문하지 않은 경우
                visitedN[loc3] = visitedN[loc] + 1
                que.append(loc3)


n, k = map(int, input().split())

BFS(n, k)
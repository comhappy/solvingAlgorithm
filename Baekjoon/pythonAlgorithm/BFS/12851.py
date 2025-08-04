# 숨바꼭질2

from collections import deque

def BFS(n, k):
    if n == k:  # 이동이 필요없는 경우
        print(0)
        print(1)

        return
    
    que = deque()
    visied = [0 for _ in range(100001)]
    que.append(n)
    visied[n] = 1

    answer_len = 0
    answer_sec = 100001

    while(que):
        
        print(que)
        x = que.popleft()
        
        if answer_sec < visied[x]:  # 최소 시간을 넘은 경우
            print(answer_sec - 1)
            print(answer_len)

            return

        if x == k:  # 정답처리 부분
            answer_len += 1
            answer_sec = visied[x]

        for i in [x - 1, x + 1, 2 * x]:
            if 0 <= i <= 100000 and (visied[i] == 0 or visied[i] == visied[x] + 1):
                que.append(i)
                visied[i] = visied[x] + 1


n, k = map(int, input().split())
BFS(n, k)
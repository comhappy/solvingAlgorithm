# A > B

from collections import deque

def BFS(a, b):
    if a == b:  # 연산이 필요없는 경우
        return 1
    else:   # BFS를 통해서 연산
        depth = 1
        que = deque()
        que.append([a, depth])

        while(que):
            num, depth = que.popleft()

            num1 = num * 2
            num2 = num * 10 + 1

            if num1 == b or num2 == b:  # 정답인 경우
                return depth + 1
            
            if num1 <= b:
#                if num1 not in que:  # 방문여부 검사
                    que.append([num1, depth + 1])

            if num2 <= b:
#                if num2 not in que:
                    que.append([num2, depth + 1])
        
        return -1   # 정답이 없는 경우

a, b = map(int, input().split())

count = BFS(a, b)

print(count)
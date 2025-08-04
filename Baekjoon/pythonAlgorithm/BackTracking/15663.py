# N과 M(9)

# 정답
# def DFS():
#     global answer, flag_num

#     if len(answer) == M:
#         for i in answer:
#             print(i, end=' ')
#         print()

#         return
#     else:
#         for i in range(0, N):
#             if visited[i] == False and num[i] != flag_num: # 방문하지 않은 경우, 중복을 제거
#                 answer.append(num[i])
#                 visited[i] = True
#                 flag_num = -1

#                 DFS()

#                 flag_num = answer.pop()
#                 visited[i] = False
        
#         return

def DFS():
    global answer, flag_num

    if len(answer) == M:
        for i in answer:
            print(i, end=' ')
        print()

        return
    else:
        for i in range(0, N):
            if visited[i] == False: # 방문하지 않은 경우, 중복을 제거
                answer.append(num[i])
                visited[i] = True
                flag_num = -1

                DFS()

                flag_num = answer.pop()
                visited[i] = False
        
        return

N, M = map(int, input().split())
num = list(map(int, input().split()))
visited = [False for _ in range(N)]

num.sort()   # 사전순 출력을 위한 정렬
answer = list()

flag_num = -1

DFS()

# N과 M(6)

def DFS(index):
    if len(answer) == M:    # 정답인 경우
        print(" ".join(map(str,answer)))
    else:
        for i in range(index, N):
            if num[i] not in answer:    # 중복을 제거
                answer.append(num[i])
                DFS(i)
                answer.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
answer =list()

DFS(0)
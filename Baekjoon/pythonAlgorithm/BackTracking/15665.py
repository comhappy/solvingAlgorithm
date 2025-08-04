# N과 M(11)

import sys
input = sys.stdin.readline

def DFS():
    global pre_num

    if len(result) == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(0, N):
            if pre_num != num[i]: # 방문하지 않은 경우
                result.append(num[i])
                pre_num = -1
                DFS()
                pre_num = result.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
result = list()
pre_num = -1

DFS()
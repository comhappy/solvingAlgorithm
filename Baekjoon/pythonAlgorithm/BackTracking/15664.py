# N과 M(10)

import sys
sys.stdin.readline

def DFS(index): # index는 추가하려는 num의 index
    global pre_num

    if len(A) == M:
        print(" ".join(map(str, A)))

        return
    else:
        for i in range(index, N):
            if pre_num != num[i]:
                A.append(num[i])
                pre_num = -1    # append, append 되는 경우를 생각해서 숫자 초기화
                DFS(i + 1)
                pre_num = A.pop()
        return


N, M = map(int, input().split())
num = list(map(int, input().split()))

num.sort()  # 오름차순을 위한 정렬

A = list()

pre_num = -1
DFS(0)
# N과 M(12)

import sys
sys.stdin.readline


def DFS(index):
    global pre_num

    if len(num) == M:
        print(" ".join(map(str, num)))
        
        return
    else:
        for i in range(index, N):   # 이전에 pop한 숫자를 다시 append하면 중복된 수열이 발생함.
            if A[i] != pre_num:     # 이때, append해서 중복된 수열이 발생할 수 없기 때문에 초기화 해줌.
                num.append(A[i])
                pre_num = -1
                DFS(i)
                pre_num = num.pop()

        return


N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()  # 오름차순을 위한 정렬

num = list()
pre_num = -1

DFS(0)
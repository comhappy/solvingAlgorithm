# 가장 긴 증가하는 부분 수열 4

import copy

n = int(input())
A = list(map(int, input().split()))

answer = [[] for _ in range(n)]
answer[0].append(A[0])
index = 0   # 정답 인덱스

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]: # 증가하는 경우
            if len(answer[j]) + 1 > len(answer[i]) + 1:
                answer[i] = copy.deepcopy(answer[j])

    answer[i].append(A[i])

    if len(answer[index]) < len(answer[i]): # 새로운 부분수열이 큰 경우
        index = i

print(len(answer[index]))
print(*answer[index])
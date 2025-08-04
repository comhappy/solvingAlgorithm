# 수 정렬하기3
# N의 개수가 10,000,000 이므로 O(nlogn)보다 작은 시간복잡도를 가지는 알고리즘을 사용해야함
# raidx sort(기수 정렬), counting sort(계수 정렬)

import sys
from collections import deque   # 수 정렬을 위해 dequeue 사용

def countingsort(S):
    R = [0] * len(S)
    result = list()

    # S를 순회하면서 값에 해당하는 index에 1 더해주기
    for i in range(len(S)):
        index = S[i]
        R[index] += 1

    # 1로 표시된 index에 해당하는 값 추가해주기
    for i in range(len(R)):
        while(R[i] != 0):
            #result.append(i)
            print(i)
            R[i] -= 1

    return result


def radixsort(S):
    # 0 ~ 9 자리수를 의미하는 큐 생성
    dequeue0 = deque()
    dequeue1 = deque()
    dequeue2 = deque()
    dequeue3 = deque()
    dequeue4 = deque()
    dequeue5 = deque()
    dequeue6 = deque()
    dequeue7 = deque()
    dequeue8 = deque()
    dequeue9 = deque()

    # 1의 자리부터 max자리까지 확인 후 큐에 추가
    max = 0

    for i in range(len(S)):
        if S[i] > max:
            max = S[i]

    length = 0  # 최대 자릿수

    while max < 0:
        max //= 10
        length += 1

    for i in range(length, -1, -1):
        S = (S // 10 ** i)
        print(S)


    return 0



N = int(sys.stdin.readline())
S = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    S[i] = num

result = radixsort(S)

# for i in range(N):
#     num = int(sys.stdin.readline())
#     S[num] += 1

# for i in range(len(S)):
#     while(S[i] != 0):
#         print(i)
#         S[i] -= 1

#result = countingsort(S)

# for i in result:
#     print(i)
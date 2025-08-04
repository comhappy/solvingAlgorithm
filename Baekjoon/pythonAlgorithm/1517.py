# 버블정렬에서 swap의 횟수를 구하는 문제
# N의 범위가 1~500,000이고 시간제한이 1초 이므로 O(nlogn)의 시간복잡도로 해결

import sys

result = 0

def mergesort(low, high):
    global result   #결과값을 global 함수로 선언

    if high == low: # 합병정렬하려고하는 원소가 1개인 경우
        return [S[low]]
    
    mid = (low + high) // 2

    A = mergesort(low, mid)
    B = mergesort(mid + 1, high)

    resultlist = list()

    # 분리된 원소 합치기
    i, j = 0, 0 # 투포인터로 사용할 index

    # B에 속한 원소가 resultlist로 이동할때 A에 남은 원소만큼 result에 더해주어야함
    while(i < len(A) and j < len(B)):
        if A[i] <= B[j]:
            resultlist.append(A[i])
            i += 1
        else:
            result += (len(A)- i)   # 정답을 계산하는 부분
            resultlist.append(B[j])
            j += 1

    # 비교가 안된 나머지 list 추가해주기
    while(i < len(A)):
        resultlist.append(A[i])
        i += 1

    while(j < len(B)):
        resultlist.append(B[j])
        j += 1

    return resultlist


N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

SR = mergesort(0, len(S)-1)

print(result)
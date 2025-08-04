#merge sort를 사용한 수 정렬

import sys

def mergesort(start, end):
    #원소가 2개 이상이면 집합 나누기(divide)
    mid = (start + end) // 2

    if end - start > 0:
        listA = mergesort(start, mid) #시작 ~ 중간
        listB = mergesort(mid + 1, end) #중간 ~ 끝
    else:   #나누기가 다 된 상태, 원소가 1개인 상황, 바로 return 해줌
        return [S[start]]

    listreturn = list() #return 할 list 생성

    #집합 합치기(merge)
    i, j = 0, 0 #투포인터로 활용할 index

    while(i < len(listA) and j < len(listB)):   #투포인터 개념
        if listA[i] < listB[j]:
            listreturn.append(listA[i])
            i += 1
        else:
            listreturn.append(listB[j])
            j += 1

    #비교하고 남은 나머지 부분들 합쳐주기
    for k in range(i, len(listA)):
        listreturn.append(listA[k])
    
    for k in range(j, len(listB)):
        listreturn.append(listB[k])
    
    return listreturn


N = int(sys.stdin.readline())
S = [0] * N

for i in range(N):
    S[i] = int(sys.stdin.readline())
    #S.append(int(input()))

S = mergesort(0, N - 1)

for i in range(N):
    print(S[i])
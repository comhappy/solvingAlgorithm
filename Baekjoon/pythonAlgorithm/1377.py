#버블정렬의 안쪽 루프가 몇번 발생하였는지 확인하는 문제

N = int(input())
A = list()

#A에 원소와 index를 리스트 형태로 추가 (element, index)
for i in range(N):
    A.append((int(input()), i))

sorted_A = sorted(A)
#sorted_A.sort()    #A를 nlogn의 시간복잡도로 정렬

Max = 0

#정렬 전, 정렬 후 Index 비교 후 최댓값 갱신
for i in range(N):
    if Max < sorted_A[i][1] - i:  #정렬 전 index - 정렬 후 index
        Max = sorted_A[i][1] - i

print(Max + 1)
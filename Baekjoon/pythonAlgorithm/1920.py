# 이진 탐색을 활용한 수 찾기

def binary_search(s, e, v): # 시작, 종료, 목표값
    # 모두 해당하지 않는 경우(리스트에 찾는 값이 없는 경우), start와 end가 역전이 되어버리는 경우
    if s >= e: 
        if A[s] == v:
            return 1
        else:
            return 0

    mid = (s + e) // 2

    if A[mid] == v:
        return 1
    elif A[mid] > v:    # 중간값이 찾는 값 보다 크면 왼쪽을 이진탐색
        return binary_search(s, mid - 1, v)
    elif A[mid] < v:    # 중간값이 찾는 값 보다 작으면 오른쪽을 이진탐색
        return binary_search(mid + 1, e, v)
    

N = int(input())
A = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

# 숫자 정렬
A.sort()

# 이진 탐색
for i in check:
    print(binary_search(0, len(A) - 1, i))
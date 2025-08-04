#퀵정렬을 사용하여 숫자를 정렬

#quick sort
def quickSort(low, high):
    """ 
    if((high - low) <= 0):    #원소의 개수가 1개이하 일때 return
        return
     """
    #pivot index 구하기
    mid = partition(low, high)
    
    #quickSort 재귀함수 호출
    if (mid == (K - 1)):
        return
    elif (mid > (K- 1)):
        quickSort(low, mid - 1)
    else:
        quickSort(mid + 1, high)

    
    #일반적인 quicksort
""" 
    quickSort(0, mid - 1)
    quickSort(mid + 1, high)
 """

def partition(low, high):   #pivot을 기준으로 두개의 집합으로 나눔
    start = low

    #데이터가 2개인 경우
    if (high - low) == 1 :
        if A[low] > A[high]:
            temp = A[low]
            A[low] = A[high]
            A[high] = temp

        return high

    pivot_index = (high + low) // 2  #중앙에 존재하는 값을 pivot으로 설정
    pivot = A[pivot_index]

    #계산의 편리성을 위해 pivot을 첫번째로 이동
    temp = A[pivot_index]
    A[pivot_index] = A[low]
    A[low] = temp

    low += 1

    while(low <= high):
        while(pivot > A[low] and low < len(A) - 1):    #low에 해당하는 값이 pivot 값보다 작은 경우
            low += 1
        
        while(pivot < A[high] and high > 0):   #high에 해당하는 값이 pivot 값보다 큰 경우
            high -= 1

        #low의 값과 high의 값 swap
        if low <= high:
            temp = A[low]
            A[low] = A[high]
            A[high] = temp
            low += 1
            high -= 1

    #pivot위치 조정
    A[start] = A[high]
    A[high] = pivot

    return high

N, K = map(int, input().split())    #split(), map() 함수를 사용하여 입력 저장
A = list(map(int, input().split()))

quickSort(0, (len(A) - 1))

print(A[K-1])
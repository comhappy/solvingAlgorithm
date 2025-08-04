""" 
def quickSort2(A):
    if len(A) <= 1:
        return A
    
    pivot = A[-1]
    leftArr, midArr, rightArr = list(), list(), list()

    for i in range(len(A)):
        if A[i] > pivot:
            rightArr.append(A[i])
        elif A[i] < pivot:
            leftArr.append(A[i])
        else:
            midArr.append(A[i])

    return quickSort(leftArr) + midArr + quickSort(rightArr)

print(quickSort([1,5,3,6,3,6]))
"""

def quickSort(A):
    def sort(low, high):
        #종료되는 조건
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = A[high-1]

        while low <= high:
            while A[low] < pivot:
                low += 1
            
            while A[high] > pivot:
                high -= 1

            #swap 해주는 과정
            if low <= high:
                A[low], A[high] = A[high], A[low]
                low += 1
                high -= 1
        
        return low
    
    sort(0, len(A) - 1)

    return A
    
print(quickSort([5,4,3,6,5,4]))
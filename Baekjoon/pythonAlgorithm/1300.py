# K번째 수
# N x N 크기의 2차원 배열(A)을 1차원배열(B)로 만들고 오름차순 정렬했을 때, B[k]의 값을 구하는 문제

# 손으로 써보는게 중요함. 여기서는 찾고자하는 수 B[k]보다 작은 수가 몇개(s)인지 확인
# if s > k: 더 작은 범위에서 탐색해야함, s < k 인경우는 반대로 생각

def binary_serach(s, e): # 이진 탐색 실행
    ans = 0

    while(s <= e):
        mid = (s + e) // 2    
        
        # m보다 작은 원소의 개수(x)를 구하기
        x = 0

        for i in range(1, n + 1):
            x += min(mid // i, n)   # 둘 중 작은값이 m보다 작은 원소의 개수가 됨

        # x를 기준으로 이진 탐색 판단
        if x >= k:
            ans = mid
            e = mid - 1     
        else:
            s = mid + 1    
    
    return ans
        

n = int(input())
k = int(input())

print(binary_serach(1, k))
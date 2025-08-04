# greedy 알고리즘

N, K = map(int, input().split())

A = [0] * N
answer = 0

# 오름차순으로 리스트 구성
for i in range(N):
    A[N-1-i] = int(input())

for i in A: # 해 선택
    ea = K // i

    if ea == 0:   # 해가 안되는 경우
        continue
    else:
        K = K - i * ea  # 해가 가능한 경우, 금액을 빼줌
        answer += ea

    if K == 0:  # 금액에 도달한 경우 종료
        break

print(answer)
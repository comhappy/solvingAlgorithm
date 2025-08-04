# 부분수열의 합

def DFS(num_index): # num_index에 해당하는 값을 추가
    global sum, result

    sum += num[num_index]

    if sum == S:
        result += 1
    
    for i in range(num_index + 1, N):
        DFS(i)
    
    sum -= num[num_index]


N, S = map(int, input().split())
num = list(map(int, input().split()))

sum, result = 0, 0

for i in range(N):
    DFS(i)

print(result)
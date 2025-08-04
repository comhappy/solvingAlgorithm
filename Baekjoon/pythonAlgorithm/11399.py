#데이터를 정렬하는 문제, 여기서는 선택정렬을 사용해보겠음

N = int(input())

time = list(map(int, input().split(' ')))

for i in range(1, N):   #1~N까지 정렬할 원소 선택
    selnum = time[i]

    #선택한 값의 자리를 찾는 과정
    for j in range(i-1, -1, -1):  
        if time[j] >= selnum:  #삽입하려고 하는 값이 작거나 같으면 넘어가기
            time[j + 1] = time[j] #shift 연산      
            time[j] = selnum      
        else:                   #삽입하려고 하는 값이 크면 넘어가기
            break

#각 사람에 대한 대기시간(t), 총 대기시간의 합(result)
t = 0
result = 0

for i in range(N):
    t = t + time[i]
    result += t

print(result)


#각 사람에 대한 대기시간(S), 총 대기시간의 합(result) → 합배열로 구하기
S = [0] * N
S[0] = time[0]

for i in range(N-1):
    S[i+1] = S[i] + time[i+1]

print(S, sum(S))
#선택정렬을 구현하라, 시간복잡도는 O(N^2)

N = list(input())

#문자형을 숫자형으로 변형
for i in range(len(N)):
    N[i] = int(N[i])

for i in range(len(N) - 1): #swap 하는 횟수
    max = N[i]
    max_index = i
    for j in range(i, len(N)):    # i ~ N 까지 반복      
        if max < N[j]:  #최소값 찾기(오름차순), 최대값 찾기(내림차순)
            max = N[j]
            max_index = j
    
    #최소값과 정렬안된 부분의 맨 앞의 값을 swap
    temp = N[max_index]
    N[max_index] = N[i]
    N[i] = temp

for i in range(len(N)):
    print(N[i], end="")
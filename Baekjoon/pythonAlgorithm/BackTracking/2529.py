# 부등호

import sys
input = sys.stdin.readline

def DFS(num):
    global max_num, min_num

    if len(number) == (k + 1):
        result = int("".join(map(str, number)))

        if result > int(max_num):
            max_num = "".join(map(str, number))
        
        if result < int(min_num):
            min_num = "".join(map(str, number))

        return
    else:
        if len(number) == 0:    # A[] 리스트를 순회할 수 없기 때문에 number에 숫자 추가
            for i in range(10):
                if visited_num[i] == False:
                    visited_num[i] = True
                    number.append(i)
                    DFS(i)
                    number.pop()
                    visited_num[i] = False

        elif A[len(number) - 1] == "<": # 오른쪽 수가 커야하는 경우
            for i in range(10):
                if visited_num[i] == False and number[-1] < i:  # 오른쪽 수가 커야함
                    visited_num[i] = True
                    number.append(i)
                    DFS(i)
                    number.pop()
                    visited_num[i] = False
        
        elif A[len(number) - 1] == ">": # 왼쪽 수가 커야하는 경우
            for i in range(10):
                if visited_num[i] == False and number[-1] > i:  # 왼쪽 수가 커야함
                    visited_num[i] = True
                    number.append(i)
                    DFS(i)
                    number.pop()
                    visited_num[i] = False
    

k = int(input())
A = list(input().split())

visited_num = [False for _ in range(10)] # 0 ~ 9 까지 선택여부를 나타내는 배열
number = list() # 결과 숫자를 나타내는 리스트

max_num, min_num = "0", "9999999999"    # 초기값 설정을 어떤 기준으로 할까?

DFS(0)

print(max_num)
print(min_num)